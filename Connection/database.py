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
        print("")
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


#  -----------------// function for the contact page-----------------//
def create_contact_page_func():
    try:
        database_cursor = my_connection.cursor()
        sql = ("CREATE TABLE contact("
               "contact_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,"
               "first_name VARCHAR(50) NOT NULL,"
               "last_name VARCHAR(50) NOT NULL,"
               "email VARCHAR(50) NOT NULL,"
               "phone_number VARCHAR(50) NOT NULL,"
               "event_name VARCHAR(50) NOT NULL,"
               "ordering_number VARCHAR(50) NOT NULL,"
               "message VARCHAR(50) NOT NULL)")
        database_cursor.execute(sql)
        my_connection.connect()
        print("contact table created successfully".capitalize())
    except Exception as ex:
        print(ex)


#  --------------// function to save the payment details-----------//
def create_table_payment_details():
    try:
        database_cursor = my_connection.cursor()
        sql = ("CREATE TABLE payments("
               "payment_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,"
               "amount VARCHAR(50) NOT NULL,"
               "currency VARCHAR(50) NOT NULL,"
               "source VARCHAR(50) NOT NULL,"
               "description VARCHAR(50) NOT NULL)")
        database_cursor.execute(sql)
        my_connection.connect()
        print("payment table created successfully".capitalize())
    except Exception as ex:
        print(ex)


def create_table_payment():
    try:
        database_cursor = my_connection.cursor()
        sql = ("CREATE TABLE payment_details("
               "payment_details_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,"
               "first_name VARCHAR(50) NOT NULL,"
               "last_name VARCHAR(50) NOT NULL,"
               "email VARCHAR(50) NOT NULL,"
               "phone_number VARCHAR(50) NOT NULL,"
               "event_name VARCHAR(50) NOT NULL,"
               "ticket_type VARCHAR(50) NOT NULL,"
               "amount VARCHAR(50) NOT NULL,"
               "currency VARCHAR(50) NOT NULL,"
               "source VARCHAR(50) NOT NULL,"
               "cvv VARCHAR(50) NOT NULL,"
               "xpr VARCHAR(50) NOT NULL,"
               "added_date VARCHAR(50) NOT NULL)")
        database_cursor.execute(sql)
        my_connection.connect()
        print("payment table created successfully".capitalize())
    except Exception as ex:
        print(ex)
