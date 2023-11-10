import mysql.connector

#  ---------the function to create the new table here-------------//
try:
    my_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="MalawiEntertainers"
    )
    if my_connection:
        print("connected successfully")
    else:
        print("failed to connect with the database")
except Exception as ex:
    print(ex)


# -----------------// functions for the table will be here---------------//
def create_events_table():
    try:
        database_cursor = my_connection.cursor()
        sql = ("CREATE TABLE events("
               "event_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,"
               "event_name VARCHAR(50) NOT NULL,"
               "date_time VARCHAR(50) NOT NULL,"
               "location VARCHAR(50) NOT NULL,"
               "description VARCHAR(50) NOT NULL,"
               "agenda VARCHAR(50) NOT NULL)")
        database_cursor.execute(sql)
        my_connection.connect()
        print("table created successfully".capitalize())
    except Exception as ex:
        print(ex)
