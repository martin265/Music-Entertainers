import flet as ft
from reportlab.lib.pagesizes import letter, legal, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from Connection.database import my_connection
from reportlab.lib.styles import getSampleStyleSheet


class ProducingReport(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.conn = my_connection
        self.cursor = self.conn.cursor()
        self.data_from_mysql = self.fetch_data_from_mysql(self.cursor)

    def fetch_data_from_mysql(self, cursor):
        sql_query = "SELECT first_name, last_name, phone_number, event_name, amount FROM payment_details"
        cursor.execute(sql_query)
        return cursor.fetchall()

    def generate_pdf_report(self, data, title, filename='report.pdf', chunk_size=400):
        pdf_doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []

        # Add a title to the page
        title_style = getSampleStyleSheet()['Title']
        title_text = Paragraph(title, title_style)
        elements.append(title_text)
        elements.append(Spacer(1, 12))  # Add some space after the title

        # Create a table header
        table_data = [['first name', 'last name', 'phone_number', 'event_name', 'amount']]
        table_data.extend(data[:chunk_size])  # Add the first chunk to the table

        while len(table_data) > 1:
            # Create a table with data (limited by chunk size)
            table = Table(table_data, colWidths=[60 * inch for inch in [2, 2, 2]])

            # Style the table
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            table.setStyle(style)
            elements.append(table)
            elements.append(Spacer(1, 12))  # Add some space between tables

            # Move to the next chunk of data
            table_data = [['first name', 'last name', 'phone_number', 'event_name', 'amount']]
            table_data.extend(data[chunk_size:chunk_size + chunk_size])

        # Build the PDF document
        pdf_doc.build(elements)
        self.generate_pdf_report(self.data_from_mysql, filename='large_data_report.pdf', chunk_size=400,
                                 title="Music Entertainers")

    def trigger_report(self, e):
        try:
            self.generate_pdf_report(
                data=self.data_from_mysql,
                title="Music entertainers"
            )
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "report generated successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
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


class FinancialReports(ft.UserControl):
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

        #   ----------------------// producing the report here//----------------------//
        self.report = ProducingReport(page=page)

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,

            controls=[
                ft.Container(
                    margin=ft.margin.only(left=20),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "financial report".capitalize(),
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                color="#0050C1"
                            )
                        ]
                    )
                ),

                #  --------------------// the financial report will be here------------//
                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(top=10),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=30, bottom=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.payment_details.payments_table
                                    ]
                                )
                            )
                        ]
                    )
                ),
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(left=30, top=10, bottom=30),
                    content=ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                width=300,
                                height=60,
                                on_click=self.report.trigger_report,
                                autofocus=True,
                                color="white",
                                bgcolor="#212121",
                                elevation=None,
                                icon=ft.icons.PICTURE_AS_PDF_ROUNDED,
                                text="generate report".capitalize(),
                                tooltip="generate report".capitalize()
                            )
                        ]
                    )
                ),

                ft.Container(
                    height=90
                )
            ]
        )
