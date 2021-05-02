from config.configuration import engine
import pandas as pd


def info_capitulo_nombre(nombre):
    query = f"""
    SELECT Episode_title AS Title, Summary, Name as Director, Stars,Votes
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
    query = f"""
    SELECT Episode_title AS Title, Summary, Name as Director, Stars,Votes
    FROM episodes AS e
    LEFT JOIN directors AS d
    ON e.Director_id = d.Director_id
    LEFT JOIN ranking AS r
    ON e.Episode_id = r.Episode_id
    LEFT JOIN seasons AS s
    ON s.Season_id = e.Season_id
    WHERE Season = {numero}
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")  

def episodios_director(nombre):
    query = f"""
    SELECT Episode_title AS Title, Name, Stars
    FROM episodes AS e
    LEFT JOIN directors AS d
    ON e.Director_id = d.Director_id
    LEFT JOIN ranking AS r
    ON e.Episode_id = r.Episode_id
    WHERE name = "{nombre}"
    """

    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")