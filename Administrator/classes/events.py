import json
from Connection.database import my_connection


class Events:
    def __init__(self, event_name, date_time, location, description, agenda):
        self.event_name = event_name
        self.date_time = date_time
        self.location = location
        self.description = description
        self.agenda = agenda
        self.database_cursor = my_connection.cursor()

    def create_event_func(self):
        try:
            sql = "INSERT INTO events(event_name, date_time, location, description, agenda) VALUES (%s, %s, %s, %s, %s)"
            values = (self.event_name, self.date_time, self.location, self.description, self.agenda)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)
