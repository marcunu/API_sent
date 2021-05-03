from config.configuration import engine
import pandas as pd


def info_capitulo_nombre(nombre):
    '''
    This function returns information from episodes by chapter name
    Args:
        -nombre: chapter name
    '''

    query = f"""
    SELECT Episode_Numer, Episode_title AS Title, Name as Director, Summary, Stars, Votes, SIA
    FROM episodes AS e
    LEFT JOIN directors AS d
    ON e.Director_id = d.Director_id
    LEFT JOIN ranking AS r
    ON e.Episode_id = r.Episode_id
    WHERE Episode_title = "{nombre}"
    """

    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")    

def info_capitulo_temporada(numero):
    '''
    This function returns information from episodes by season number
    Args:
        -numero: season number
    '''

    query = f"""
    SELECT s.Season, Episode_Number, Episode_title AS Title, Summary, Name, Stars,SIA
    FROM episodes AS e
    LEFT JOIN directors AS d
    ON e.Director_id = d.Director_id
    LEFT JOIN ranking AS r
    ON e.Episode_id = r.Episode_id
    LEFT JOIN seasons AS s
    ON s.Season_id = s.Season_id
    WHERE s.Season = {numero}
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")  

def episodios_director(nombre):
    '''
    This function returns episodes done by a selected director
    Args:
        -nombre: Director name
    '''

    query = f"""
    SELECT Name, s.Season, Episode_Number, Episode_title AS Title, Year, Stars, SIA
    FROM episodes AS e
    LEFT JOIN directors AS d
    ON e.Director_id = d.Director_id
    LEFT JOIN ranking AS r
    ON e.Episode_id = r.Episode_id
    LEFT JOIN seasons AS s
    ON e.Season_id = s.Season_id
    WHERE name = "{nombre}"
    """

    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")

def info_director(nombre):
    '''
    This function returns information from directors table
    Args:
        -nombre: director name
    '''

    query = f"""
    SELECT Name, Director_id, Episodes
    FROM directors
    WHERE Director_id = "{nombre}"
    """

    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")

def info_season(num):
    '''
    This function returns information from seasons table
    Args:
        -num: season number
    '''

    query = f"""
    SELECT Season_id, Season, Year, Episodes
    FROM seasons
    WHERE Season = {num}
    """

    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")        


def toda_informacion():
    '''
    This function returns all information from the database
    '''

    query = f"""
    SELECT s.Season, Episode_Number, Episode_title AS Title, Name AS Director, Duration, Summary, Year, Stars, Votes, SIA
    FROM episodes AS e
    LEFT JOIN directors AS d
    ON e.Director_id = d.Director_id
    LEFT JOIN ranking AS r
    ON e.Episode_id = r.Episode_id
    LEFT JOIN seasons AS s
    ON e.Season_id = s.Season_id
    """

    data = pd.read_sql_query(query, engine)
    return data.to_json(orient='records')