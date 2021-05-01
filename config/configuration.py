import os 
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()

password = os.getenv("sql_pass")
dbName = "HP"

connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"

engine = alch.create_engine(connectionData)