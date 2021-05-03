#This python file downloads a dataset from kaggle, clean it and add a sentiment analysis.


#Import necessary libraries 

import pandas as pd
import tools.functions as fun

###regex
import re

###NLTK
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

###TextBlob
from textblob import TextBlob

###SpaCy
import spacy
from spacy import displacy
print("Libraries imported succesfully")

#Download DataFrame
df = fun.download_kaggle()

print("DataFrame downloaded succesfully")
#----------------------------------------------------------

#Make a Sentiment Analysis of each episodes

## Add a column where each word is a element of a list
nltk.download("punkt")
df["token"] = df.Summary.apply(fun.token)

## Delete all the 'Stop Words' from the list
nltk.download("stopwords")
df.token = df.token.apply(fun.stop_words)

## Make the sentiment Analysis of the summary of each episode
df["SIA"] = df.token.apply(fun.sent_analysis)

## Save the DataFrame
df.to_csv("data/friends_sia.csv")


print("Sentiment Analysis done succesfully")
#-------------------------------

data = df

data["Episode ID"] = data.apply(lambda row: f"{row['Season']}_{row['Episode Number']}", axis = 1)

data["Season ID"] = data.apply(lambda row: f"s_{row['Season']}", axis = 1)

data["Summary"] = data["Summary"].apply(fun.quitar_comillas)

data["Director ID"] = data.apply(lambda row: f"DI_{row['Director'][0]}{row['Director'][1]}{row['Director'][-2]}", axis = 1)

#data["Episode Number"] = data.apply(lambda row: f"e_{row['Episode Number']}", axis = 1)

#--------------------------------
#Creation of different dataframes for the SQL DataBase tables.

#Seasons
temporadas = data.loc[:,["Season ID","Episode Number"]].groupby("Season ID").count()
temporadas.to_csv("data/temporadas.csv")

#Episodes
episodes = data.loc[:,["Episode ID","Season","Season ID","Director ID", "Episode Number","Episode_Title","Duration","Summary","SIA"]]
episodes.to_csv("data/episodios.csv")

#Directors
a = data["Director"].value_counts()
name = list(a.keys())
epi = list(a.values)
director = pd.DataFrame(list(zip(name,epi)), columns = ['Name','Number of episodes'])
director["Director ID"] = director.apply(lambda row: f"DI_{row['Name'][0]}{row['Name'][1]}{row['Name'][-2]}", axis = 1)
director.to_csv("data/director.csv")

#Ranking
rank = data.loc[:,["Episode ID","Stars","Votes","SIA"]]
rank.to_csv("data/rank.csv")

print("Dataframes created succesfully")





