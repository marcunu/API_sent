<img src="https://habrastorage.org/webt/t6/sr/jr/t6srjrmjjmm6qn8gpld9emy4txu.gif" class="center">


# API Sentiment Project

This project consists of the creation of a database using `Flask` to create it, add information and consult it by means of APIs.

<img src="https://media1.tenor.com/images/60e825ea5be132c7b511adea590a9e10/tenor.gif?itemid=12296269" class="center">

For this I have created a database in `SQL` with the information of the different seasons of `Friends`, this database includes:
* Episodes
* Directors 
* Summary
* Seasons
* Rates & Votes

# Index

* Documents
* Steps
* APIs
* Programms
* Python libraries



# Documents

* 01 - **Kaggle.py**: Data collection executable and `Sentimen Analysis` of data.
* 02 - **SQL Jupyter**: database creation from jupyter.
* 03 - **Visualization**
* 04 - Draft Notebooks:
    * Kaggle.
    * Sentiment Analysis.



# Steps

* `Step 1`: Select the dataset from  [Kaggle](https://www.kaggle.com/rezaghari/friends-series-dataset?select=friends_episodes_v3.csv)
        
* `Step 2`: make the sentiment analysis of the data.

* `Step 3`: Clean-up the dataset and export it in `.csv` format..

* `Step 4`: take the information obtained in the two previous steps and add it to `SQL DataBase`.

* `Step 5`: create the necessary `endpoints` to get or post information.




# APIs

Different APIs are created in order to allow the clients get or post information, some of this APIs are:

* Get: this method give information to the client.
    * [Get episodes by name](http://localhost:5000/episodes_name/)
    * [Get episodes by director](http://localhost:5000/episodes_by_director/)
    
* POST: this method allows the client to post information.
    * [POST new director](http://localhost:5000/new_director/")
    * [POST new episode](http://localhost:5000/new_episode/)
    

# Sentiment Analysis

Using `NLP & Text Sentiment Analysis` I made an emotional analysis of the data, finding out which are the most and the least emotional episodes from the different seasons of `Friends`.
    


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
* Nltk
* textblob
* spacy
* Personal function library (getdata, postdata,functions,...)