import psycopg2
# Establish a connection to the PostgreSQL database
from dotenv import load_dotenv
import os
load_dotenv()

PASS = os.getenv("PASS")
conn = psycopg2.connect(
    dbname='dataquesttest',
    user='postgres',
    password=PASS,
    host='localhost',
    port=5432
)
