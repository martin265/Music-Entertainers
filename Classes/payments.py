import flet as ft
import os
from Connection.database import my_connection


class Payment:
    def __init__(self, amount, currency, source, description):
        self.amount = amount
        self.currency = currency
        self.source = source
        self.description = description
        self.database_cursor = my_connection.cursor()

    #  ----------------// function to save payment details to the database-------//
    def save_payment_details_func(self):
        try:
            sql = "INSERT INTO payments(amount, currency, source, description) VALUES (%s, %s, %s, %s)"
            values = (self.amount, self.currency, self.source, self.description)
            self.database_cursor.execute(sql, values)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)