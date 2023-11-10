import flet as ft


class MainDashboard(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

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
                )
            ]
        )
