#Countguy
> AKA the person who keeps a track of everything you do


##What?
This was built to solve a problem for my friend. He is not a programmer but he loves to solve small problems in his team that can be solved through building in-house apps. The easiest way to get these "small" apps approved is by keeping a count of how many times it has been used. Initially there was only one app but as he started exploring more processes, it turned out that there were more apps that could be built -- Hence this. 

**Countguy** is a simple server where he can _create_ apps that he can track and all that he needs to do is keep incrementing the count on _that_ app. Problem solved

The rest of the document is for him and how to install it :D

##Installation

###Cloning Countguy

* Open up git and type this command in the directory where you want the project (it creates a folder for you): `git clone git@github.com:shrayas/countguy.git`
* After the clone is successful, you should see a directory called `countguy`

###Virtualenv

* Now create a virtual environment in this directory.
* Open up command prompt and browse to the `countguy` directory that you just cloned down
* type `virtualenv env` at the prompt and you should see some progress.
* Once that is done, type `env\bin\activate` and you should see `(env)` come up in the prompt

###Install packages

* Now that you're in the environment (you should see the `(env)` in your prompt), you have to install the packages required for the app to run
* Type `pip install -r requirements.txt` and it will go through the file and install the required packages

###Creating the database

* In the `countguy` directory type `python`. This should take you to a python interpreter. You should see a `>` prompt
* here type the following commands

		from app import initializeDB
		initializeDB()
* Type `quit()` to quit the python intrepreter