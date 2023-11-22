import flet as ft


class ClientDetails(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.first_name = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="first name".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.NAME,
            color="#311B92",
        )

        #  --------------------// ----------------------------//
        self.last_name = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="last name".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#311B92",
            keyboard_type=ft.KeyboardType.NAME,
            color="#311B92",
        )

        self.email = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="email".capitalize(),
            label_style=ft.TextStyle(
                color="#0078D9"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#311B92",
            keyboard_type=ft.KeyboardType.NAME,
            color="#311B92",
        )

        #  --------------------// ----------------------------//
        self.phone_number = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.PHONE_ANDROID_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="numbers only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="phone number".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#311B92",
            keyboard_type=ft.KeyboardType.NAME,
            color="#311B92",
        )

        self.event_name = ft.Dropdown(
            width=480,
            height=100,
            prefix_icon=ft.icons.EVENT_NOTE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="event name",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="event name".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="#311B92",

            options=[
                ft.dropdown.Option("Summer Dance"),
                ft.dropdown.Option("music"),
                ft.dropdown.Option("Rap showcasing"),
            ]
        )

        self.ticket_type = ft.Dropdown(
            width=480,
            height=100,
            prefix_icon=ft.icons.AIRPLANE_TICKET_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="ticket type".capitalize(),
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="ticket type".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="#311B92",

            options=[
                ft.dropdown.Option("diamond".capitalize()),
                ft.dropdown.Option("gold".capitalize()),
                ft.dropdown.Option("silver"),
            ]
        )

    def build(self):
        return ft.ListView()


class PaymentDetails(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        #  ------------------------//--------------------//
        self.amount = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.MONEY_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="numbers only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="amount".capitalize(),
            label_style=ft.TextStyle(
                color="#0078D9"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#311B92",
            keyboard_type=ft.KeyboardType.NAME,
            color="#311B92",
        )

        #  --------------------// ----------------------------//
        self.phone_number = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.PHONE_ANDROID_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="numbers only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="phone number".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#311B92",
            keyboard_type=ft.KeyboardType.NAME,
            color="#311B92",
        )

        self.currency = ft.Dropdown(
            width=480,
            height=100,
            prefix_icon=ft.icons.CURRENCY_POUND_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="select your currency",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#311B92",
            label="currency".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="#311B92",
            options=[
                ft.dropdown.Option("Dollar"),
                ft.dropdown.Option("Kwacha"),
            ],
        )

        #  -----------  // getting the amount and the actual currency here----//
        self.source = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,

            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.CREDIT_CARD_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="numbers only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0078D9",
            label="card token".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.NUMBER,
            color="#311B92",
        )

        #  -----------  // getting the amount and the actual currency here----//
        self.cvv = ft.TextField(
            width=240,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.TOKEN_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0078D9",
            label="CVV".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.NUMBER,
            color="#311B92",
        )

        #  -----------  // getting the amount and the actual currency here----//
        self.xpr = ft.TextField(
            width=240,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.TIMELAPSE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0078D9",
            label="expire".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.NUMBER,
            color="#311B92",
        )

    def build(self):
        return ft.ListView(

        )


class InitialisePaymenytDetails(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.ListView()


class PaymentView(ft.UserControl):
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

        #  -------------------// getting the values from the main class  //-----------------//
        self.client_details = ClientDetails(page=page)

        #   -----------------------// payment details //--------------------------//
        self.payment_details = PaymentDetails(page=page)

    def InitialisePaymentDetails(self, e):
        try:
            if not self.client_details.first_name.value:
                self.client_details.first_name.error_text = "fill in the blanks first".capitalize()
                self.page.update()

        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,

            controls=[
                ft.Container(
                    margin=ft.margin.only(top=30),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "ticket payment".capitalize(),
                                color="#212121",
                                font_family="Raleway",
                                style=ft.TextThemeStyle.DISPLAY_SMALL
                            )
                        ]
                    )
                ),

                #  ----------------// the cards will be here //-----------------------//
                ft.Container(
                    margin=ft.margin.only(top=30),
                    content=ft.Row(
                        controls=[
                            #  ------------// first card for the container here------//
                            ft.Container(
                                width=400,
                                height=540,
                                margin=ft.margin.only(left=30),
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#311B92",
                                        "#0078D9"
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right
                                ),
                                shadow=ft.BoxShadow(
                                    blur_radius=9,
                                    blur_style=ft.ShadowBlurStyle.INNER,
                                    color="#311B92",
                                ),
                                border_radius=ft.border_radius.all(10),
                                content=ft.Column(
                                    controls=[
                                        #  -----------// for the image here
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.DIAMOND_ROUNDED,
                                                        size=100,
                                                        color="white"
                                                    )
                                                ]
                                            )

                                        ),

                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "diamond tickets".capitalize(),
                                                        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                        color="white"
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ----------------// the text for the card here ----------//
                                        ft.Container(
                                            margin=ft.margin.only(left=20, right=20, top=10),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "Premium Seating: Diamond ticket holders"
                                                        " often enjoy better seating arrangements"
                                                        " with improved views of the event, whether"
                                                        " it's a concert, sports game,"
                                                        " or theater performa "
                                                        "Diamond tickets might provide access to"
                                                        " the best seats in the venue, offering an "
                                                        "unparalleled view of the stage for an optimal"
                                                        " concert experience",
                                                        color="white",
                                                        font_family="Raleway",
                                                        size=20
                                                    )
                                                ]
                                            )
                                        ),

                                        #  --------------// container for the button here-------//
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=150,
                                                        height=60,
                                                        on_click={},
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#212121",
                                                        elevation=None,
                                                        icon=ft.icons.QR_CODE_ROUNDED,
                                                        text="qr code".capitalize(),
                                                        tooltip="schedule your ticket".capitalize()
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),

                            #  --------------------// the second card container will be here---------//
                            #  ------------// first card for the container here------//
                            ft.Container(
                                width=400,
                                height=540,
                                margin=ft.margin.only(left=30),
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#1A237E",
                                        "#004FA6"
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right
                                ),
                                shadow=ft.BoxShadow(
                                    blur_radius=9,
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                    color="white",
                                ),
                                border_radius=ft.border_radius.all(10),
                                content=ft.Column(
                                    controls=[
                                        #  -----------// for the image here
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.MONEY_ROUNDED,
                                                        size=100,
                                                        color="white"
                                                    )
                                                ]
                                            )

                                        ),

                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "gold tickets".capitalize(),
                                                        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                        color="white"
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ----------------// the text for the card here ----------//
                                        ft.Container(
                                            margin=ft.margin.only(left=20, right=20, top=10),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "Premium Seating: Gold ticket holders"
                                                        " often enjoy better seating arrangements"
                                                        " with improved views of the event, whether"
                                                        " it's a concert, sports game,"
                                                        " or theater performa "
                                                        "Gold tickets might provide access to"
                                                        " the best seats in the venue, offering an "
                                                        "unparalleled view of the stage for an optimal"
                                                        " concert experience",
                                                        color="white",
                                                        font_family="Raleway",
                                                        size=20
                                                    )
                                                ]
                                            )
                                        ),

                                        #  --------------// container for the button here-------//
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=150,
                                                        height=60,
                                                        on_click={},
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#212121",
                                                        elevation=None,
                                                        icon=ft.icons.QR_CODE_ROUNDED,
                                                        text="qr code".capitalize(),
                                                        tooltip="schedule your ticket".capitalize()
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),

                            #  ------------------------// last card --------------------//
                            #  ------------// first card for the container here------//
                            ft.Container(
                                width=400,
                                height=540,
                                margin=ft.margin.only(left=30),
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#5951A9",
                                        "#835CAF"
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right
                                ),
                                shadow=ft.BoxShadow(
                                    blur_radius=9,
                                    blur_style=ft.ShadowBlurStyle.INNER,
                                    color="#311B92",
                                ),
                                border_radius=ft.border_radius.all(10),
                                content=ft.Column(
                                    controls=[
                                        #  -----------// for the image here
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.CURRENCY_BITCOIN_ROUNDED,
                                                        size=100,
                                                        color="white"
                                                    )
                                                ]
                                            )

                                        ),

                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "silver tickets".capitalize(),
                                                        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                        color="white"
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ----------------// the text for the card here ----------//
                                        ft.Container(
                                            margin=ft.margin.only(left=20, right=20, top=10),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "Premium Seating: Silver ticket holders"
                                                        " often enjoy better seating arrangements"
                                                        " with improved views of the event, whether"
                                                        " it's a concert, sports game,"
                                                        " or theater performa "
                                                        "Silver tickets might provide access to"
                                                        " the best seats in the venue, offering an "
                                                        "unparalleled view of the stage for an optimal"
                                                        " concert experience",
                                                        color="white",
                                                        font_family="Raleway",
                                                        size=20
                                                    )
                                                ]
                                            )
                                        ),

                                        #  --------------// container for the button here-------//
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=150,
                                                        height=60,
                                                        on_click={},
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#212121",
                                                        elevation=None,
                                                        icon=ft.icons.QR_CODE_ROUNDED,
                                                        text="qr code".capitalize(),
                                                        tooltip="schedule your ticket".capitalize()
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),

                        ]
                    )
                ),

                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Book and pay".capitalize(),
                                color="#212121",
                                font_family="Raleway",
                                style=ft.TextThemeStyle.DISPLAY_SMALL
                            )
                        ]
                    )
                ),

                #  --------------------// container for the payment details here---------//
                ft.Container(
                    width=1000,
                    height=750,
                    margin=ft.margin.only(left=100, right=100, top=30),
                    border_radius=ft.border_radius.all(10),
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        blur_style=ft.ShadowBlurStyle.OUTER,
                        color="#311B92",

                    ),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=40),
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                self.client_details.first_name,
                                                self.client_details.last_name
                                            ]
                                        ),

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                self.client_details.email,
                                                self.client_details.phone_number
                                            ]
                                        ),

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                self.client_details.event_name,
                                                self.client_details.ticket_type
                                            ]
                                        ),

                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "card details",
                                                        color="#212121",
                                                        font_family="Raleway",
                                                        style=ft.TextThemeStyle.DISPLAY_SMALL
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
                                                            self.payment_details.amount,
                                                            self.payment_details.currency
                                                        ]
                                                    ),

                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            self.payment_details.source,
                                                            self.payment_details.cvv,
                                                            self.payment_details.xpr
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),

                                        # ----------------// container for the button //--------------//
                                        ft.Container(
                                            margin=ft.margin.only(left=100),
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=200,
                                                        height=60,
                                                        on_click=self.InitialisePaymentDetails,
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#212121",
                                                        elevation=None,
                                                        icon=ft.icons.QR_CODE_ROUNDED,
                                                        text="buy ticket".capitalize(),
                                                        tooltip="buy your ticket".capitalize()
                                                    )
                                                ]
                                            )
                                        )

                                    ]
                                )
                            )
                        ]
                    )
                ),

                #  ------------------------//
                ft.Container(
                    height=300
                )
            ]
        )
