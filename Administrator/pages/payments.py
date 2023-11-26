import flet as ft
from Connection.database import my_connection


class CalculateSilverPrices(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()
        self.total_amount = ft.Text()

    def calculate_silver_tickets(self):
        try:
            sql = "SELECT amount FROM payment_details WHERE ticket_type = %s"
            values = ("Silver",)
            self.database_cursor.execute(sql, values)

            all_results = self.database_cursor.fetchall()

            # Extract and convert amounts to numbers
            amounts = [float(result[0]) for result in all_results if result[0].replace('.', '').isdigit()]

            # Calculate the total
            self.total_amount = sum(amounts)
        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView()


class CalculateDiamondPrices(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()
        self.total_amount = ft.Text()

    def calculate_diamond_tickets(self):
        try:
            sql = "SELECT amount FROM payment_details WHERE ticket_type = %s"
            values = ("Diamond",)
            self.database_cursor.execute(sql, values)

            all_results = self.database_cursor.fetchall()

            # Extract and convert amounts to numbers
            amounts = [float(result[0]) for result in all_results if result[0].replace('.', '').isdigit()]

            # Calculate the total
            self.total_amount = sum(amounts)
        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView()


class CalculateTicketPrices(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()

    def calculate_tickets(self):
        try:
            sql = "SELECT amount FROM payment_details WHERE ticket_type = %s"
            values = ("Gold",)
            self.database_cursor.execute(sql, values)

            all_results = self.database_cursor.fetchall()

            # Extract and convert amounts to numbers
            amounts = [float(result[0]) for result in all_results if result[0].replace('.', '').isdigit()]

            # Calculate the total
            total_amount = sum(amounts)

            print("Total Amount:", total_amount)


        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView()


class FetchPaymentsDetails(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()
        self.payments_table = ft.DataTable(
            width=1200,
            horizontal_margin=10,
            sort_column_index=0,
            # height=700,
            sort_ascending=True,
            column_spacing=5,
            bgcolor="white",
            heading_text_style=ft.TextStyle(
                size=15,
                weight=ft.FontWeight.BOLD,
                color="#311B92",
            ),
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(1, "#f5f5f5"),
            columns=[
                ft.DataColumn(ft.Text("first name".capitalize())),
                ft.DataColumn(ft.Text("last name".capitalize())),
                ft.DataColumn(ft.Text("email".capitalize())),
                ft.DataColumn(ft.Text("phone number".capitalize())),
                ft.DataColumn(ft.Text("event name".capitalize())),
                ft.DataColumn(ft.Text("ticket type".capitalize())),

                ft.DataColumn(ft.Text("amount".capitalize())),
                ft.DataColumn(ft.Text("currency".capitalize())),
                ft.DataColumn(ft.Text("added date".capitalize())),

            ],
            rows=[]
        )

    def fetch_payments(self):
        try:
            sql = "SELECT * FROM payment_details"
            self.database_cursor.execute(sql)
            all_results = self.database_cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in self.database_cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]

            for single_record in rows:
                self.payments_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(single_record["first_name"])),
                            ft.DataCell(ft.Text(single_record["last_name"])),
                            ft.DataCell(ft.Text(single_record["email"][:10])),
                            ft.DataCell(ft.Text(single_record["phone_number"])),
                            ft.DataCell(ft.Text(single_record["event_name"])),

                            ft.DataCell(ft.Text(single_record["ticket_type"])),
                            ft.DataCell(ft.Text(single_record["amount"])),

                            ft.DataCell(ft.Text(single_record["currency"])),
                            ft.DataCell(ft.Text(single_record["added_date"])),
                            #  --------------the delete and update controls------------//
                        ]
                    )
                )
        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView()


class Payments(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.page.padding = 0
        self.page.spacing = 0
        self.page.fonts = {
            "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
            "Raleway": "assets/fonts/static/Raleway-Light.ttf",
            "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
            "Roboto-black": "assets/fonts/Roboto-Black.ttf",
            "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
        }

        self.payment_details = FetchPaymentsDetails(page=page)

        #  -------------// function that callas the payments details here //------------//
        self.payment_details.fetch_payments()

        #  -------------------// calculations //---------------------//
        self.payments_calculations = CalculateTicketPrices(page=page)
        self.payments_calculations.calculate_tickets()

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                # -----------// the top container will be here // -------------------//
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "payments and calculations".capitalize(),
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                color="#0050C1"
                            )
                        ]
                    )
                ),

                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(top=10),
                    content=ft.Column(
                        controls=[
                            #  ----------------// the table for all the payments details
                            ft.Container(
                                margin=ft.margin.only(left=40, right=40, top=30),
                                content=ft.Row(
                                    controls=[
                                        self.payment_details.payments_table
                                    ]
                                )
                            ),

                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        #  --------------// container for the text here //----------//
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "calculations".capitalize(),
                                                        color="#0050C1",
                                                        font_family="Raleway",
                                                        style=ft.TextThemeStyle.DISPLAY_SMALL
                                                    )
                                                ]
                                            )
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                ),

                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(top=10),
                    content=ft.Row(
                        controls=[
                            ft.Tabs(
                                scrollable=True,
                                animation_duration=10,
                                animate_size=900,
                                selected_index=0,
                                tabs=[
                                    ft.Tab(
                                        tab_content=ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.AIRPLANE_TICKET_ROUNDED,
                                                        color="#311B92"
                                                    ),
                                                    ft.Text(
                                                        "diamond tickets".title(),
                                                        weight=ft.FontWeight.W_700
                                                    )
                                                ]
                                            )
                                        ),
                                        content=ft.Container(
                                            height=700,
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[

                                                ]
                                            )
                                        ),
                                    ),
                                    #  -----------------//-----------------
                                    ft.Tab(
                                        tab_content=ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.CURRENCY_BITCOIN_ROUNDED,
                                                    ),
                                                    ft.Text(
                                                        "gold tickets".title(),
                                                        weight=ft.FontWeight.W_700
                                                    )
                                                ]
                                            )
                                        ),
                                        content=ft.Container(
                                            margin=ft.margin.only(top=20),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[

                                                ]
                                            )
                                        ),
                                    ),

                                    ft.Tab(
                                        tab_content=ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.CURRENCY_POUND_ROUNDED,
                                                    ),
                                                    ft.Text(
                                                        "silver tickets".title(),
                                                        weight=ft.FontWeight.W_700
                                                    )
                                                ]
                                            )
                                        ),
                                        content=ft.Container(
                                            margin=ft.margin.only(top=20),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[

                                                ]
                                            )
                                        ),
                                    ),
                                ],
                                width=1250,
                                height=400
                            )
                        ]
                    )
                ),

                ft.Container(
                    height=200
                )

            ]
        )
