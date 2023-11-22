import flet as ft
import datetime
import calendar
from Connection.database import my_connection

# some constants here----------//
CELL_SIZE = (28, 28)
CELL_BG_COLOR = "#0078D9"
TODAY_BG_COLOR = "#E52E6A"


#  ----------------// the custom fonts for the website will be here for the imports here----//
# -------------building the actual calendar here---//
class SetCalendar(ft.UserControl):
    """the class install will be used to get the 12 months of the calendar"""

    def __init__(self, start_year=datetime.date.today().year):
        super().__init__()
        self.current_year = start_year
        self.m1 = datetime.date.today().month
        self.m2 = self.m1 + 1
        #  -----------// tracking the clicks here----//
        self.click_count: list = []  # for tracking click count
        self.long_press_count: list = []  # same as above
        self.database_cursor = my_connection.cursor()
        self.current_color = "blue"
        self.selected_date = any

        self.calendar_grid = ft.Column(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        )

    #   ----------------// function to allow the pagination of the calendar here----------//
    def calendar_pagination_func(self, delta):
        """the function will be responsible for paginating content"""
        try:
            self.m1 = min(max(1, self.m1 + delta), 12)
            self.m1 = min(max(2, self.m2 + delta), 13)
            #  ---------------// variable for a new calendar-------------//
            new_calendar = self.create_month_calendar(self.current_year)
            self.calendar_grid = new_calendar
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

    #  ----------------// function will be trigger the hover effect---------------//
    def container_hover(self, e):
        calendar_pop = ft.SnackBar(
            content=ft.Container(
                height=90,
                content=ft.Text(
                    "hello world"
                )
            )
        )
        self.page.snack_bar = calendar_pop
        calendar_pop.open = True
        self.page.update()

    #  -----------------getting the alert dialog for the available event here-------------//
    def available_events(self, e):
        try:
            current_date = e.control.data
            current_event = ft.AlertDialog(
                content=ft.Container(
                    bgcolor="white",
                    border_radius=ft.border_radius.all(10),
                    height=500,
                    width=800,
                    content=ft.Column(
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            #  --------------// the header container here---------//
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src="assets/images/events/calendar.png",
                                            height=200,
                                            width=300
                                        )
                                    ]
                                )
                            ),
                            #  ----------------// container for the date here-----------//
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "upcoming event at",
                                            weight=ft.FontWeight.W_700,
                                            color="#0050C1",
                                            size=24
                                        ),
                                        ft.Divider(height=10),
                                        ft.Text(
                                            f"{current_date}",
                                            weight=ft.FontWeight.W_700,
                                            color="#0050C1",
                                            size=20,
                                        )
                                    ]
                                )
                            ),
                            #  -----------------// getting the event here---------------//
                            ft.Container(
                                margin=ft.margin.only(left=20, right=20),
                                content=ft.Column(
                                    controls=[
                                        #  --------------// the top main container here------//
                                        ft.Text(
                                            "At Music entertainers, we understand that a seamless and"
                                            " secure payment process is crucial for our valued customers."
                                            " That's why we offer a variety of payment methods to ensure"
                                            " your shopping experience is as smooth and hassle-free as "
                                            "possible. Whether you prefer traditional payment options or "
                                            "the latest digital solutions, we've got you covered.",
                                            color="black",
                                            size=20,
                                            text_align=ft.alignment.center,
                                        ),
                                        #  ------------// the container for the buttons here-----//
                                        ft.Container(
                                            margin=ft.margin.only(top=20, bottom=20),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=250,
                                                        height=70,
                                                        bgcolor="#0050C1",
                                                        text="price".capitalize(),
                                                        icon=ft.icons.PRICE_CHANGE_ROUNDED,
                                                        icon_color="white",
                                                        color="white"
                                                    ),

                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
            self.page.dialog = current_event
            current_event.open = True
            self.page.update()
        except Exception as e:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                f"something went wrong at ".format(e)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  ---------------//
    def get_all_events_func(self, e):
        current_date = e.control.data
        #sql = ("SELECT event_name, location FROM events WHERE date_time=%s", current_date)
        self.database_cursor.execute('SELECT * from events WHERE date_time = %s', current_date)
        all_results = self.database_cursor.fetchall()
        print(all_results)

    #  ----------// the logic for the calendar here--------//
    def create_month_calendar(self, year):
        global month_grid
        self.current_year = year  # ----current year
        self.calendar_grid.controls: list = []

        for month in range(self.m1, self.m2):
            month_label = ft.Text(
                f"{calendar.month_name[month]} {self.current_year}",
                size=24,
                weight=ft.FontWeight.W_700,
                text_align=ft.alignment.center,
            )
            #  -----month matrix here--------//
            month_matrix = calendar.monthcalendar(self.current_year, month)
            month_grid = ft.Column(
                alignment=ft.MainAxisAlignment.CENTER
            )
            #  ---------------//----------------------//
            month_grid.controls.append(
                ft.Container(
                    margin=ft.margin.only(left=35),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            month_label
                        ]
                    )
                )
            )
            #  ---------// getting the weeks here for the calendar----------//
            weekday_labels = [
                ft.Container(
                    width=100,
                    height=100,
                    alignment=ft.alignment.center,

                    content=ft.Text(
                        weekday,
                        size=20,
                        color="#4A148C",
                        weight=ft.FontWeight.W_700
                    )
                )
                for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            ]
            #  --------------// getting the week days in a row here---------//
            weekday_row = ft.Row(controls=weekday_labels)
            month_grid.controls.append(weekday_row)

            #  ----------------// passing for the days here----------------//
            for week in month_matrix:
                week_container = ft.Row()
                for day in week:
                    if day == 0:
                        day_container = ft.Container(
                            width=100,
                            height=100,
                        )
                    else:
                        day_container = ft.Container(
                            width=100,
                            height=100,
                            ink=False,
                            # on_hover=self.container_hover,
                            border=ft.border.all(0.3, color="#4A148C"),
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(10),
                            #  ----------passing additional parameters to the container here-----//
                            data=datetime.date(
                                year=self.current_year,
                                day=day,
                                month=month
                            ),
                            on_click=self.get_all_events_func,
                            on_long_press=lambda e: self.show_two_dates(e),
                            animate=400,
                            # ------------// content for the boxes----------//
                        )
                    day_label = ft.Text(
                        str(day),
                        size=24,
                        color="black",
                        weight=ft.FontWeight.W_700,
                    )
                    #  ------------// making the second checks here--------//
                    if day == 0:
                        day_label = None
                    if (
                            day == datetime.date.today().day
                            and month == datetime.date.today().month
                            and self.current_year == datetime.date.today().year
                    ):
                        # day_label.bgcolor = "teal700"
                        day_container.bgcolor = "#4A148C"
                    day_container.content = day_label
                    week_container.controls.append(day_container)
                #  ------------// appending controls to the container here--------------//
                month_grid.controls.append(week_container)

        self.calendar_grid.controls.append(
            month_grid,
        )
        return self.calendar_grid

    def build(self):
        return self.create_month_calendar(self.current_year)


#  ------------------// the date and month setups here------------------//
class DateSetUp(ft.UserControl):
    """the class for the grid controls here"""

    def __init__(self, cal_grid):
        super().__init__()
        self.cal_grid = cal_grid

        #   ---------------// buttons for the pagination will be here for the system-----------//
        self.prev_button = ButtonPagination("Prev", None)
        self.next_button = ButtonPagination("Next", None)
        #  ------------// getting the day here----------//
        self.today = ft.Text(
            datetime.date.today().strftime("%B, %d, %Y"),
            width=260,
            size=34,
            color="white24",
            weight=ft.FontWeight.W_700
        )
        #  ------------// the button container here-------------//
        self.btn_container = ft.Container(
            #  --------------this will hold the pagination for the buttons----------//
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    self.prev_button,
                    self.next_button
                ]
            )
        )


#  ---------------page pagination will be here for the website------------------//
class ButtonPagination(ft.UserControl):
    def __init__(self, txt_name, function):
        super().__init__()
        self.txt_name = txt_name
        self.function = function

    def build(self):
        return ft.IconButton(
            width=56,
            height=28,
            on_click=self.function,
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=6)},
                bgcolor="#212121"
            )
        )


#  ------------------// the function that will handle the calendar pagination's here----------//


#  ---------------// the function for the calendar component for the client to select-----//

class EventsView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.calendar = SetCalendar()
        self.database_cursor = my_connection.cursor()
        self.page.spacing = 0
        self.page.margin = 0
        #  ----------------// the custom fonts for the website will be here for the imports here----//
        self.page.fonts = {
            "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
            "Raleway": "assets/fonts/static/Raleway-Light.ttf",
            "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
            "Roboto-black": "assets/fonts/Roboto-Black.ttf",
            "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
        }
        # help me God to figure this thing out please help sir"""
        self.date_picker = ft.DatePicker(
            first_date=datetime.datetime(2023, 10, 1),
            last_date=datetime.datetime(2024, 10, 1),
        )
        page.overlay.append(self.date_picker)

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  ---------------// the main container for the website here------------//
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=20, bottom=10),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Container(
                                            margin=ft.margin.only(left=55),
                                            content=ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        "check your event".capitalize(),
                                                        font_family="Raleway-bold",
                                                        size=24,
                                                        color="#0050C1"
                                                    ),
                                                ]
                                            )
                                        ),
                                        #  -------------// the calendar for the events will be here------//
                                        ft.Container(
                                            margin=ft.margin.only(right=55),
                                            content=ft.Row(
                                                controls=[
                                                    ft.IconButton(
                                                        bgcolor="#311B92",
                                                        icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                                        icon_color="white",
                                                        on_click=lambda _: self.date_picker.pick_date()
                                                    )
                                                ]
                                            )
                                        )

                                    ]
                                )

                            ),
                            #  ------------// the container for the center text here----------//
                            #  ----------------// the main calendar will be down here for the system------------//
                            ft.Container(
                                margin=ft.margin.only(bottom=400),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        #  ----------// the container to wrap the calendar here
                                        ft.Container(
                                            width=1200,
                                            height=730,
                                            bgcolor="white",
                                            border_radius=ft.border_radius.all(10),
                                            shadow=ft.BoxShadow(
                                                blur_radius=9,
                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                color="#311B92",
                                            ),
                                            content=ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                self.calendar
                                                            ]
                                                        )
                                                    ]
                                                )
                                            )
                                        )
                                    ]
                                )
                            ),
                            #  ----------------// container for the ticket ranges----------//
                        ]
                    )
                )
            ]
        )
