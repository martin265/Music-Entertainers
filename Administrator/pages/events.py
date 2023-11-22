import flet as ft
import datetime
from Administrator.classes.events import Events
from Connection.database import my_connection


class EventsPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.current_date = ft.Text()
        self.database_cursor = my_connection.cursor()
        self.editDelete_id = ft.Text()
        #  -------------// getting input details from the users--------------//
        self.event_name = ft.TextField(
            width=550,
            height=90,
            border_color="#311B92",
            helper_text="characters only",
            hint_text="event name",
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.EVENT_AVAILABLE_ROUNDED,
            label="event name".capitalize(),
        )
        #  --------------------//thank you God//-------------------//
        self.agenda = ft.TextField(
            width=550,
            height=90,
            border_color="#311B92",
            helper_text="characters only",
            hint_text="agenda",
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.VIEW_AGENDA_ROUNDED,
            label="agenda".capitalize(),
        )
        #  --------------------//thank you God//-------------------//
        self.description = ft.TextField(
            width=550,
            height=90,
            border_color="#311B92",
            helper_text="characters only",
            hint_text="description".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.EVENT_AVAILABLE_ROUNDED,
            label="description".capitalize(),
        )
        #  --------------------//thank you God//-------------------//
        self.location = ft.Dropdown(
            width=550,
            height=90,
            border_color="#311B92",
            helper_text="characters only",
            hint_text="description".capitalize(),
            prefix_icon=ft.icons.EVENT_AVAILABLE_ROUNDED,
            label="location".capitalize(),
            options=[
                ft.dropdown.Option("blantyre".capitalize()),
                ft.dropdown.Option("lilongwe".capitalize()),
                ft.dropdown.Option("zomba".capitalize()),
                ft.dropdown.Option("mangochi".capitalize()),
            ]
        )
        #  --------------------//thank you God//-------------------//
        self.date_time = ft.ElevatedButton(
            width=200,
            height=60,
            on_click=lambda _: self.date_picker.pick_date(),
            icon_color="white",
            bgcolor="#311B92",
            tooltip="select date",
            text="select event date".capitalize(),
            elevation=0,
            color="white",
            style=ft.ButtonStyle(
                color="white",
            ),
            icon=ft.icons.DATE_RANGE_ROUNDED
        )
        #  -----------------// the date here---------------------//
        self.date_picker = ft.DatePicker(
            on_change=self.get_current_date,
            first_date=datetime.datetime(2023, 10, 1),
            last_date=datetime.datetime(2024, 10, 1)
        )
        self.page.overlay.append(self.date_picker)
        #  ---------------// the events table will be here-----------------//
        self.events_table = ft.DataTable(
            width=1200,
            horizontal_margin=10,
            sort_column_index=0,
            height=400,
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
                ft.DataColumn(ft.Text("operations".capitalize())),

            ],
            rows=[]
        )
        #  -------------------// contact table here--------------//
        self.contact_table = ft.DataTable(
            width=1200,
            horizontal_margin=10,
            sort_column_index=0,
            height=400,
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
                ft.DataColumn(ft.Text("ordering number".capitalize())),
                ft.DataColumn(ft.Text("message".capitalize())),
                ft.DataColumn(ft.Text("operations".capitalize())),
            ],
            rows=[]
        )
        #  -------------------// update modal here------------//
        self.events_update_modal = ft.AlertDialog(
            title=ft.Text(
                "update event".capitalize(),
                style=ft.TextThemeStyle.HEADLINE_SMALL,
                color="#311B92",
            ),
            title_padding=ft.padding.only(left=30, top=30),
            content=ft.Container(
                bgcolor="white",
                width=600,
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    auto_scroll=True,
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Image(
                                        src="assets/stickers/update.png",
                                        height=100,
                                        width=100
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.event_name,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.date_time,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.location,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.description,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.agenda,
                                        ]
                                    ),

                                ]
                            )
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=20, bottom=10),
                            content=ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        width=200,
                                        height=60,
                                        on_click=self.update_events_func,
                                        icon_color="white",
                                        bgcolor="#311B92",
                                        tooltip="update event",
                                        text="update event".capitalize(),
                                        elevation=0,
                                        color="white",
                                        style=ft.ButtonStyle(
                                            color="white",
                                        ),
                                        icon=ft.icons.UPDATE_ROUNDED
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
        )

    #  --------------------// functions to get the actual dates here---------//
    def change_date(self, e):
        print(self.date_picker.value)

    #  --------------// getting the actual date----------//
    def get_current_date(self, e):
        self.current_date = self.date_picker.value

    #  --------------------// function to validate the input fields here---------//
    def validate_inputs_func(self, e):
        try:
            if not self.event_name.value:
                self.event_name.error_text = "enter event name".capitalize()
                self.update()
            #  --------------------//-----------------------------//
            elif not self.description.value:
                self.description.error_text = "add something".capitalize()
                self.update()
            #  ---------------------------//------------------------//
            elif not self.location.value:
                self.location.error_text = "select location first".capitalize()
                self.update()
            #  ----------------------------//------------------------//
            elif not self.agenda.value:
                self.agenda.error_text = "add agenda".capitalize()
                self.update()
            else:
                self.save_events_func()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  -------------------// function for saving the details to the database---------//
    def save_events_func(self):
        try:
            #  ------// getting the time here-------//
            events = Events(
                self.event_name.value,
                self.current_date,
                self.location.value,
                self.description.value,
                self.agenda.value
            )
            events.create_event_func()
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#311B92",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "events details saved successfully".capitalize(),
                                color="white",
                                size=20
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.update()
            self.show_events_table()
            self.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  -------------------// functions for the modals here-------------//
    def trigger_events_update_modal(self, e):
        try:
            self.page.dialog = self.events_update_modal
            self.events_update_modal.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    def build(self):
        self.show_events_table()
        self.show_contacts_table()
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  --------------// the main container for the events page-------//
                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(top=10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "events page".capitalize(),
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            color="#311B92"
                                        )
                                    ]
                                )
                            ),
                            #  ------------// container for the input controls here----//
                            ft.Container(
                                margin=ft.margin.only(top=40, left=70),
                                content=ft.Column(
                                    controls=[
                                        ft.Row([self.event_name, self.agenda]),
                                        ft.Row([self.description, self.location]),
                                        ft.Container(
                                            margin=ft.margin.only(right=80),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.END,
                                                controls=[
                                                    self.date_time
                                                ]
                                            ),
                                        ),
                                        #  ------------------// the container for the buttons
                                        ft.Container(
                                            margin=ft.margin.only(bottom=20),
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=200,
                                                        height=60,
                                                        on_click=self.validate_inputs_func,
                                                        icon_color="white",
                                                        bgcolor="#311B92",
                                                        tooltip="create event",
                                                        text="create event".capitalize(),
                                                        elevation=0,
                                                        color="white",
                                                        style=ft.ButtonStyle(
                                                            color="white",
                                                        ),
                                                        icon=ft.icons.CREATE_ROUNDED
                                                    ),
                                                    #  ------------//-------//

                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),

                        ]
                    )
                ),
                #  -----------------// container for the
                ft.Container(
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
                                                        ft.icons.EVENT_AVAILABLE_ROUNDED,
                                                        color="#311B92"
                                                    ),
                                                    ft.Text(
                                                        "events".title(),
                                                        weight=ft.FontWeight.W_700
                                                    )
                                                ]
                                            )
                                        ),
                                        content=ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    self.events_table
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
                                                        ft.icons.CONTACT_MAIL_ROUNDED,
                                                    ),
                                                    ft.Text(
                                                        "contacts".title(),
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
                                                    self.contact_table
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
                )
            ]
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
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.UPDATE_ROUNDED,
                                        on_click=self.fill_text_boxes,
                                        tooltip="update",
                                        icon_color="#00B4C6",
                                    ),
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.DELETE_ROUNDED,
                                        on_click=self.delete_event_func,
                                        tooltip="delete",
                                        icon_color="#f44336"
                                    ),
                                    #  ------------------deleting and updating the records-------//
                                ]
                            )
                        ),

                    ]
                )
            )

    #  ----------------------// function to get all the contacts details here----//
    def show_contacts_table(self):
        sql = "SELECT * FROM contact"
        self.database_cursor.execute(sql)
        all_results = self.database_cursor.fetchall()
        #  ----------pushing the data to the main table here----------------//
        columns = [column[0] for column in self.database_cursor.description]
        rows = [dict(zip(columns, row)) for row in all_results]
        for single_record in rows:
            self.contact_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(single_record["first_name"])),
                        ft.DataCell(ft.Text(single_record["last_name"])),
                        ft.DataCell(ft.Text(single_record["email"][:10])),
                        ft.DataCell(ft.Text(single_record["phone_number"])),
                        ft.DataCell(ft.Text(single_record["event_name"])),
                        ft.DataCell(ft.Text(single_record["ordering_number"])),
                        ft.DataCell(ft.Text(single_record["message"])),
                        #  --------------the delete and update controls------------//
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.UPDATE_ROUNDED,
                                        on_click={},
                                        tooltip="update",
                                        icon_color="#00B4C6",
                                    ),
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.DELETE_ROUNDED,
                                        on_click={},
                                        tooltip="delete",
                                        icon_color="#f44336"
                                    ),
                                    #  ------------------deleting and updating the records-------//
                                ]
                            )
                        ),

                    ]
                )
            )

    #  -----------------//-----------------------------------//
    def fill_text_boxes(self, e):
        """the function to prefill the text-boxes when the button is clicked here-------"""
        try:
            self.editDelete_id = e.control.data["event_id"]
            self.event_name.value = e.control.data["event_name"]
            self.date_time = e.control.data["date_time"]
            self.location.value = e.control.data["location"]
            self.description.value = e.control.data["description"]
            self.agenda.value = e.control.data["agenda"]
            self.page.dialog = self.events_update_modal
            self.events_update_modal.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="red",
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title(),
                        color="white",
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  -----------------// the function will be used to update the records-------//
    def update_events_func(self, e):
        """the function to update the records here"""
        try:
            #  ------// getting the time here-------//
            events = Events(
                self.event_name.value,
                self.current_date,
                self.location.value,
                self.description.value,
                self.agenda.value
            )
            events.update_event_func(self.editDelete_id)
            self.show_events_table()
            self.page.update()
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#311B92",
                content=ft.Container(
                    content=ft.Text(
                        "event details updated successfully".capitalize(),
                        color="white",
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.events_update_modal.open = False
            self.page.update()

        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="red",
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title(),
                        color="white",
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  -------------------// function to delete the events here--------------//
    def delete_event_func(self, e):
        try:
            #  ------// getting the time here-------//
            events = Events(
                self.event_name.value,
                self.date_time,
                self.location.value,
                self.description.value,
                self.agenda.value
            )
            events.delete_event_func(self.editDelete_id)
            self.show_events_table()
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#311B92",
                content=ft.Container(
                    content=ft.Text(
                        "event details deleted successfully".capitalize(),
                        color="white",
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="red",
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title(),
                        color="white",
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()
