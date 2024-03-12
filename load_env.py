import os
from dotenv import load_dotenv
import mysql.connector

# Carrega as variáveis do arquivo .env no ambiente de trabalho
load_dotenv()

# A função os.getenv é usada para obter o valor das variáveis de ambiente
uri  = os.getenv("MONGODB_URI")
host = os.getenv("DB_HOST")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

print(cnx)
