import pandas as pd
import os

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