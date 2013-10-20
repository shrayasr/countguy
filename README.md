#Countguy
> AKA the person who keeps a track of everything you do

##What?
This was built to solve a problem for my friend. He is not a programmer but he loves to solve small problems in his team that can be solved through building in-house apps. The easiest way to get these "small" apps approved is by keeping a count of how many times it has been used. Initially there was only one app but as he started exploring more processes, it turned out that there were more apps that could be built -- Hence this. 

**Countguy** is a simple server where he can _create_ apps that he can track and all that he needs to do is keep incrementing the count on _that_ app. Problem solved

The rest of the document is for him and how to install it :D

##Installation

###Pre-requisites
* You need to setup Python and PIP on the system. Instructions [here](http://docs.python-guide.org/en/latest/starting/install/win/)
* You need Git as well. Get it from [here](https://msysgit.googlecode.com/files/Git-1.8.4-preview20130916.exe)

###Cloning Countguy

* Open up git and type this command in the directory where you want the project (it creates a folder for you): `git clone git@github.com:shrayas/countguy.git`
* After the clone is successful, you should see a directory called `countguy`

###Virtualenv

* Now create a virtual environment in this directory.
* Open up command prompt and browse to the `countguy` directory that you just cloned down
* type `virtualenv env` at the prompt and you should see some progress.
* **Activating the virtual env**: Once that is done, type `env\bin\activate` and you should see `(env)` come up in the prompt

###Install packages

* CD into the `countguy` directory
* Activate the virtual env
* Type `pip install -r requirements.txt` and it will go through the file and install the required packages

###Creating the database

* CD into the `countguy` directory
* Activate the virtual env (see **Virtualenv** step if you've forgotten)
* Type the command: `python initDB.py` and that should bring up a `countguy.db` in the same directory. Now an empty DB is created. 

###Running the app

* CD into the `countguy` directory
* Activate the virtual env
* Type `python app.py`

###Testing the app

* Open a browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000` and you should see a welcome message

##API

Everything with `countguy` can be done through an API. Make sure you have [Postman](https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en) installed.

###Get the counts for all the apps

* URL: `/apps/`
* Method: `GET`

###Create a new app

* URL: `/apps/`
* Method: `POST`
* Data
	* Type: `form-data` or `x-www-form-urlencoded`
	* Key: `appname`
	* Value: The name of the app you want to create 

###Get the counts for an app

* URL: `/apps/<name_of_the_app_created>`
* Method: `GET`

###Increment the count for an app

* URL: `/apps/<name_of_the_app_created>`
* Method: `POST`
* Data:
	* **NA**

###Set the count for an app

* URL: `/apps/<name_of_the_app_created>`
* Method: `PUT`
* Data:
	* Type: `form-data` or `x-www-form-urlencoded`
	* Key: `count`
	* Value: The count for the app you want to set 
	
###Delete an app

* URL: `/apps/<name_of_the_app_created>`
* Method: `DELETE`
* Data:
	* **NA**

---

![counter-image](http://www.jellycounter.com/wp-content/uploads/2012/10/counter.jpg)