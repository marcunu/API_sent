from config.configuration import engine


def insertadatos(escena, personaje, frase):
    engine.execute(f"""
    INSERT INTO frases (scene, character_name, dialogue)  VALUES
    ({escena},'{personaje}','{frase}');
    """)