# API Sentiment Project

This project consists of the creation of a database using `Flask` to create it, add information and consult it by means of APIs.

For this I have created a database in `SQL`.

# Index

* Documents
* Steps
* APIs
* Programms
* Python libraries



# Documents

* 01 - Data collection executable.
* 02 - SQL Jupyter: database creation from jupyter.
* 03 - Sentiment Analysis: graphs of the information obtained.



# Steps

* `Step 1`: Select the dataset from  [Kaggle](https://www.kaggle.com/rezaghari/friends-series-dataset?select=friends_episodes_v3.csv)
        
* `Step 2`: Clean-up the dataset and export it in `.csv` format..

* `Step 3`: take the information obtained in the two previous steps and add it to `SQL DataBase`.

* `Step 4`: create the necessary `endpoints` to get or post information.

* `Step 5`: make the sentiment analysis of the data.


# APIs

Different APIs are created in order to allow the clients get or post information, some of this APIs are:

* Get: this method give information to the client.
    * [Get episodes by name](http://localhost:5000/episodes_name/)
    * [Get episodes by director](http://localhost:5000/episodes_by_director/)
    
* POST: this method allows the client to post information.
    * [POST new director](http://localhost:5000/new_director/")
    * [Get new episode](http://localhost:5000/new_episode/)


    


# Programs

* Python
* Jupyter NoteBook
* Visual Code


# Python libraries

* Pandas
* Seaborn
* Json
* Requests
* Mathplotlib
* Numpy
* SQL Alchemy
* Getpass
* Os
* Dotenv
* Personal function library (getdata, postdata,functions,...)