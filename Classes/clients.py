import flet as ft
from Connection.database import my_connection


class ContactUs:
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 phone_number,
                 event_name,
                 ordering_number,
                 message):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.event_name = event_name
        self.ordering_number = ordering_number
        self.message = message
        self.database_cursor = my_connection.cursor()

    #  ----------// functions to save the contact details
    def save_contact_details_func(self):
        """the function will save the contact details to the database"""
        try:
            sql = "INSERT INTO contact(first_name, last_name, email, phone_number, event_name, ordering_number, message) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            values = (
                self.first_name, self.last_name, self.email, self.phone_number, self.event_name, self.ordering_number,
                self.message)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

