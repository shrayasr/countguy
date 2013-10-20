import sqlite3
import json

from flask import Flask,g,request

##### GLOBALS #####
app = Flask(__name__)
DB = 'countguy.db'
##########

##### DB FUNCTIONS #####

# Get the instance of a database
def connectDB():
    return sqlite3.connect(DB);

# Initialize the DB, see README on how to
def initializeDB():
    db = connectDB()
    with app.open_resource('schema.sql',mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Run a query on the DB
def query(query,args=(),one=False):
    cur = g.db.execute(query,args)
    rv = [dict((cur.description[index][0],value) for index, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

# Update data on the DB (inserts/updates)
def update(query):
    g.db.execute(query)
    g.db.commit()

##########

##### FLASK DECORATORS #####

# This function is executed BEFORE a request handling begins
@app.before_request
def beforeRequest():
    # get the connection to the db
    g.db = connectDB()

# This function is executed AFTER a request is handled
@app.after_request
def afterRequest(response):
    # close the db connection
    g.db.close()

    # return the response as-is
    return response

##########

##### APP FUNCTIONS #####

def createNewApp(appName):
    queryString = "INSERT INTO counts VALUES ('"+appName+"',0)"
    update(queryString)

def getAllCounts():
    queryString = "SELECT * FROM counts"
    return query(queryString)

def getAppCount(appName):
    queryString = "SELECT * FROM counts WHERE appname = '"+appName+"'"
    return query(queryString)

def incrementAppCount(appName):
    queryString = "UPDATE counts SET count = (SELECT (count+1) FROM counts WHERE appname = '"+appName+"') WHERE appname = '"+appName+"'"
    update(queryString)

def deleteApp(appName):
    queryString = "DELETE FROM counts WHERE appname = '"+appName+"'"
    update(queryString)

def setAppCount(appName, count):
    queryString = "UPDATE counts SET count = "+count+" WHERE appname = '"+appName+"'"
    update(queryString)

def appExists(appName):
    queryString = "SELECT * from counts WHERE appname = '"+appName+"'"
    countOfApps = len(query(queryString))

    return not countOfApps == 0
##########

##### ROUTES #####

@app.route("/")
def sayHello():
    return "Welcome to Countguy(tm)"

'''
    /apps/

    GET
        Get the list of counts for ALL apps
    POST
        Create a new app
'''
@app.route("/apps/", methods=['GET','POST'])
def counts():

    if request.method == 'POST':
        try:
            appName = request.form['appname'].strip()
            
            if not appExists(appName):
                createNewApp(appName)
                return json.dumps(getAppCount(appName))
            else:
                return "App already exits"
        except KeyError:
            return "invalid request"
        
    elif request.method == 'GET':
        appCounts = getAllCounts()
        if len(appCounts) == 0:
            return "No apps exist"
        else:
            return json.dumps(appCounts)

'''
    /apps/<app>/

    GET
        Get the counts for the "app"
    POST
        Increment the count for the "app" by 1
    PUT
        Set the count for the "app"
    DELETE
        Delete that app
'''
@app.route("/apps/<appName>/", methods=['GET','POST','DELETE','PUT'])
def appCounts(appName):

    appName = appName.strip()

    if request.method == 'POST':
        if not appExists(appName):
            return "App doesn't exist, create it first"
        else:
            incrementAppCount(appName)
            return json.dumps(getAppCount(appName))

    elif request.method == 'GET':
        if not appExists(appName):
            return "App doesn't exist, create it first"
        else:
            return json.dumps(getAppCount(appName))

    elif request.method == 'DELETE':
        if not appExists(appName):
            return "App doesn't exist, create it first"
        else:
            deleteApp(appName)
            return "App deleted"

    elif request.method == 'PUT':
        if not appExists(appName):
            return "App doesn't exist, create it first"
        else:
            try:
                appCount = request.form['count']
                setAppCount(appName,appCount)
                return json.dumps(getAppCount(appName))
            except KeyError:
                return "Invalid request"

##########

# MAIN PROGRAM
if __name__ == "__main__":
    app.debug = True
    app.run()
