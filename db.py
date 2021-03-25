import mysql.connector

connection = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",  # ip of the server that hosts the db
    database="ardit700_pm1database",
    buffered=True
)

