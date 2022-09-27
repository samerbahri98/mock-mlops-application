import mysql.connector
import os


loggerdb = mysql.connector.connect(
  host=os.getenv("MYSQL_HOST"),
  user=os.getenv("MYSQL_USER"),
  password=os.getenv("MYSQL_PASSWORD"),
  database=os.getenv("MYSQL_DATABASE")
)

logger_cursor = loggerdb.cursor()
