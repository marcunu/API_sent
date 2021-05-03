import pandas as pd
import os

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

