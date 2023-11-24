from Connection.database import my_connection


class PaymentTracking:
    def __init__(self, first_name, last_name, email, phone_number, event_name, ticket_type, amount, currency, source, cvv, xpr, current_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.event_name = event_name
        self.ticket_type = ticket_type
        self.amount = amount
        self.currency = currency
        self.source = source
        self.cvv = cvv
        self.xpr = xpr
        self.current_date = current_date
        self.database_cursor = my_connection.cursor()

    def save_payment_details(self):
        sql = "INSERT INTO payment_details(first_name, last_name, email, phone_number, event_name, ticket_type, amount, currency, source, cvv, xpr, added_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            self.first_name,
            self.last_name,
            self.email,
            self.phone_number,
            self.event_name,
            self.ticket_type,
            self.amount,
            self.currency,
            self.source,
            self.cvv,
            self.xpr,
            self.current_date
        )
        self.database_cursor.execute(sql, values)
        my_connection.commit()
        print("saved successfully")


# payment = PaymentTracking("martin", "silungwe", "martin@gmail.com", "0880619", "music", "gold", "1000", "kwacha", "897634434", "123", "12", "11/23/2023")
# payment.save_payment_details()
