from config.configuration import engine


def inserta_dir(dir_id, nombre, num_epi):
    '''
    This function insert data into directors table
    '''

    engine.execute(f"""
    INSERT INTO directors (Director_id, Name, Episodes)  VALUES
    ('{dir_id}','{nombre}',{num_epi});
    """)

def inserta_tempo(temp_id, temp, ano, capitulo):
    '''
    This function insert data into seasons table
    '''

    engine.execute(f"""
    INSERT INTO seasons (Season_id, Season, Year, Episodes) VALUES
    ('{temp_id}', {temp}, {ano}, {capitulo});
    """)

def inserta_epis(epi_id, sea_id, sea, dir_id, epi_num, epi_tit, dur, suma):
    '''
    This function insert data into episodes table
    '''

    engine.execute(f"""
    INSERT INTO episodes (Episode_id, Season_id, Season, Director_id, Episode_number, Episode_title, Duration, Summary)  VALUES
    ('{epi_id}','{sea_id}',{sea},'{dir_id}','{epi_num}','{epi_tit}',{dur},'{suma}');
    """)

def inserta_rank(epi_id, estre, votos, ana):
    '''
    This function insert data into ranking table
    '''

    engine.execute(f"""
    INSERT INTO ranking (Episode_id, Stars, Votes, SIA) VALUES
    ('{epi_id}',{estre},{votos},{ana});
    """)
