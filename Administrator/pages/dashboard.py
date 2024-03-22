import flet as ft
from Connection.database import my_connection


class EventsTable(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()

        self.events_table = ft.DataTable(
            width=1200,
            horizontal_margin=10,
            sort_column_index=0,
            height=500,
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
                ft.DataColumn(ft.Text("event name".capitalize())),
                ft.DataColumn(ft.Text("date".capitalize())),
                ft.DataColumn(ft.Text("location".capitalize())),
                ft.DataColumn(ft.Text("description".capitalize())),
                ft.DataColumn(ft.Text("agenda".capitalize())),
            ],
            rows=[]
        )

        #  ----------------------// the table for the events will be here--------------//

    def show_events_table(self):
        sql = "SELECT * FROM events"
        self.database_cursor.execute(sql)
        all_results = self.database_cursor.fetchall()
        #  ----------pushing the data to the main table here----------------//
        columns = [column[0] for column in self.database_cursor.description]
        rows = [dict(zip(columns, row)) for row in all_results]

        for single_record in rows:
            self.events_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(single_record["event_name"])),
                        ft.DataCell(ft.Text(single_record["date_time"])),
                        ft.DataCell(ft.Text(single_record["location"][:10])),
                        ft.DataCell(ft.Text(single_record["description"])),
                        ft.DataCell(ft.Text(single_record["agenda"])),
                        #  --------------the delete and update controls------------//
                    ]
                )
            )

    def build(self):
        return ft.ListView()


class MainDashboard(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        # ---------------------// the events table here //-------------------//
        self.events_table = EventsTable(page=page)
        self.events_table.show_events_table()

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  ---------// the main container here----//
                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(top=10),
                    content=ft.Column(
                        controls=[
                            #  -----------// the top text here------//
                            ft.Container(
                                margin=ft.margin.only(left=30, top=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "main dashboard".capitalize(),
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            color="#311B92"
                                        )
                                    ]
                                )
                            ),
                            #  -----------// container for the cards here---//
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        #  -------// first card container-------//
                                        ft.Container(
                                            margin=ft.margin.only(left=20, bottom=20, top=30),
                                            width=400,
                                            height=400,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#311B92",
                                                    "#0078D9"
                                                ],
                                                begin=ft.alignment.bottom_left,
                                                end=ft.alignment.top_right,
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    #  -----// for the top sticker-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src="assets/icons/payment.png",
                                                                    height=100,
                                                                    width=100
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  ----------// for the text-------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, right=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            wrap=True,
                                                            controls=[
                                                                ft.Text(
                                                                    "the system manages clients payments"
                                                                    "using advanced features that keeps "
                                                                    "funds in total security from malicious"
                                                                    "acts from accessing clients money".capitalize(),
                                                                    text_align=ft.alignment.center,
                                                                    color="white",
                                                                    size=20
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------------------// the page for the outlined buttons here-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30, bottom=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.OutlinedButton(
                                                                    width=250,
                                                                    height=80,
                                                                    text="stripe payment gateway".capitalize(),
                                                                    icon=ft.icons.PAYPAL_ROUNDED,
                                                                    on_click={},
                                                                    icon_color="white",
                                                                    style=ft.ButtonStyle(
                                                                        color="white"
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ----------------the other card control here-----------//
                                        ft.Container(
                                            margin=ft.margin.only(left=20, bottom=20, top=30),
                                            width=350,
                                            height=400,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#311B92",
                                                    "#A50084"
                                                ],
                                                begin=ft.alignment.bottom_left,
                                                end=ft.alignment.top_right,
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    #  -----// for the top sticker-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src="assets/contact/registration.png",
                                                                    height=100,
                                                                    width=100
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  ----------// for the text-------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, right=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            wrap=True,
                                                            controls=[
                                                                ft.Text(
                                                                    "the system has been integrated with a "
                                                                    "tool to monitor clients who have been registered "
                                                                    "with the system, the records area will"
                                                                    "provide a table that lists all the registered"
                                                                    "clients".capitalize(),
                                                                    text_align=ft.alignment.center,
                                                                    color="white",
                                                                    size=20
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------------------// the page for the outlined buttons here-------//
                                                    #  -------------------// the page for the outlined buttons here-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(bottom=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.OutlinedButton(
                                                                    width=250,
                                                                    height=80,
                                                                    text="registered clients".capitalize(),
                                                                    icon=ft.icons.PEOPLE_ROUNDED,
                                                                    on_click={},
                                                                    icon_color="white",
                                                                    style=ft.ButtonStyle(
                                                                        color="white"
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        # -----------------// the last card will be here------------------//
                                        ft.Container(
                                            margin=ft.margin.only(left=20, bottom=20, top=30),
                                            width=400,
                                            height=400,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#311B92",
                                                    "#E52E6A"
                                                ],
                                                begin=ft.alignment.bottom_left,
                                                end=ft.alignment.top_right,
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    #  -----// for the top sticker-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src="assets/stickers/podcast.png",
                                                                    height=100,
                                                                    width=100
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  ----------// for the text-------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, right=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            wrap=True,
                                                            controls=[
                                                                ft.Text(
                                                                    "the system also manages all the available events"
                                                                    "and later the events will be shown to the clients"
                                                                    "all the events will be accessed by clients "
                                                                    "in the events area of the main system".capitalize(),
                                                                    text_align=ft.alignment.center,
                                                                    color="white",
                                                                    size=20
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------------------// the page for the outlined buttons here-------//
                                                    #  -------------------// the page for the outlined buttons here-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30, bottom=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.OutlinedButton(
                                                                    width=250,
                                                                    height=80,
                                                                    text="available events".capitalize(),
                                                                    icon=ft.icons.EVENT_NOTE_ROUNDED,
                                                                    on_click={},
                                                                    icon_color="white",
                                                                    style=ft.ButtonStyle(
                                                                        color="white"
                                                                    )
                                                                )
                                                            ]
                                                        )
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
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=30, bottom=30),
                                content=ft.Row(
                                    controls=[
                                        self.events_table.events_table
                                    ]
                                )
                            )
                        ]
                    )
                ),

                ft.Container(
                    height=100
                )
            ]
        )
