import pandas as pd
import os
import requests

#NLTK
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

#nltk.download("punkt")
#nltk.download("stopwords")
#nltk.download("vader_lexicon")


def download_kaggle():
    '''
    This function downloads, unzip, delet zip file and move to data folder, a dataset from kaggle.
    Finally returns the dataset.
    Arg:
         
    '''
    #Firs of all, download the file
    os.system("kaggle datasets download -d rezaghari/friends-series-dataset")

    #we need to unzip the file
    os.system("unzip friends-series-dataset.zip")

    #Delete the zip file and the old version
    os.system("rm -rf friends-series-dataset.zip")
    os.system("rm -rf friends_episodes_v2.csv")

    #Move to data folder
    os.system("mv friends_episodes_v3.csv data/friends_episodes_v3.csv")

    data = pd.read_csv("data/friends_episodes_v3.csv")
    return data

def quitar_comillas(fila):
    return fila.replace('"',"'")

# Sentiment analysis

def token(row):
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(row)
    return tokens

def stop_words (lista):
    
    stop_words = set(stopwords.words("english"))
    nueva = []
    for w in lista:
        if w not in stop_words:
            nueva.append(w)
    return " ".join(nueva)

def sent_analysis(string):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(string)
    pol = polarity["compound"]
    return pol

def api_datos(url):
    url_data = "http://localhost:5000/" + url
    response = requests.get(url = url_data).json()
    return pd.read_json(response)

def input_director():

    dir_id = input("Introduce an id for the director: ")

    while len(dir_id)>6:
        print("Director_id must be 6 character or less.")
        input("Please, try again: ")
        break
        
    nombre = input("Introduce director´s name: ")
    episodes = input("Introduce how many episodes the director has made: ")

    nuevo_dir = {
        'Director_id':{dir_id},
        'Name':{nombre},
        'Episodes':episodes
        }

    url_dir = "http://localhost:5000/new_director"

    return requests.post(url_dir, data = nuevo_dir)


def input_season():
    temp_id = input("Introduce an id for new season: ")

    while len(temp_id)>6:
        print("Season_id must be 6 character or less.")
        input("Please, try again: ")
        break

    temp = input("Introduce a new season: ")
    ano = input("Introduce the year of the season: ")
    num = input("Introduce how many episodes the season has: ")

    nueva_temp = {'Season_id' : {temp_id},
    'Season' : {temp},
    'Year' : {ano},
    'Episodes' : {num}}

    url_temp = "http://localhost:5000/new_season"

    return requests.post(url_temp, data = nueva_temp)


