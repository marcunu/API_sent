from config.configuration import engine


def inserta_dir(dir_id, nombre, num_epi):
    engine.execute(f"""
    INSERT INTO directors (Director_id, Name, Episodes)  VALUES
    ('{dir_id}','{nombre}',{num_epi});
    """)


def inserta_epis(epi_id, sea_id, sea, dir_id, epi_num, epi_tit, dur, suma):
    engine.execute(f"""
    INSERT INTO episodes (Episode_id, Season_id, Season, Director_id, Episode_number, Episode_title, Duration, Summary)  VALUES
    ('{epi_id}','{sea_id}',{sea},'{dir_id}','{epi_num}','{epi_tit}',{dur},'{suma}');
    """)