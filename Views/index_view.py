import flet as ft


def IndexView(page):
    page.spacing = 0
    page.margin = 0

    #  ----------------// the custom fonts for the website will be here for the imports here----//
    page.fonts = {
        "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
        "Raleway": "assets/fonts/static/Raleway-Light.ttf",
        "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
        "Roboto-black": "assets/fonts/Roboto-Black.ttf",
        "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
    }
    #  --------------------------// section for the alert dialogs-----------//
    payments_modal = ft.AlertDialog(
        content=ft.Container(
            width=700,
            height=600,
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    #  -------------// the container for the image here--------//
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    width=700,
                                    height=300,
                                    border_radius=ft.border_radius.all(10),
                                    src=f"assets/images/cards/online-payment.png"
                                )
                            ]
                        )
                    ),
                    #  ----------for the top header text----------------//
                    ft.Container(
                        margin=ft.margin.only(left=20),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "payment".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    font_family="Raleway-bold",
                                    size=30,
                                    color="#0078D9"
                                )
                            ]
                        )
                    ),
                    #  -------------// for the text here---------------//
                    ft.Container(
                        margin=ft.margin.only(left=20, top=10),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "At Music entertainers, we understand that a seamless and"
                                    " secure payment process is crucial for our valued customers."
                                    " That's why we offer a variety of payment methods to ensure"
                                    " your shopping experience is as smooth and hassle-free as "
                                    "possible. Whether you prefer traditional payment options or "
                                    "the latest digital solutions, we've got you covered.",
                                    color="black",
                                    size=18,

                                )
                            ]
                        )
                    ),
                    #  ----------for the payment methods here----------------//
                    ft.Container(
                        margin=ft.margin.only(left=20),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "payment methods".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    font_family="Raleway-bold",
                                    size=30,
                                    color="#0078D9"
                                )
                            ]
                        )
                    ),
                    #  ---------------// payment methods integration---------------//
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                #  ------// the first payment method---------//
                                ft.Container(
                                    margin=ft.margin.only(left=20, top=10),
                                    content=ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                elevation=None,
                                                width=200,
                                                height=70,
                                                icon=ft.icons.PAYPAL_ROUNDED,
                                                icon_color="white",
                                                color="white",
                                                text="paypal".capitalize(),
                                                bgcolor="#0078D9",
                                            )
                                        ]
                                    )
                                )
                                #  --------------// the second payment method------//
                            ]
                        )
                    )

                ]
            )
        )
    )
    #  --------------//----------------------//
    tickets_modal = ft.AlertDialog(
        content=ft.Container(
            width=700,
            height=600,
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    #  -------------// the container for the image here--------//
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    width=700,
                                    height=300,
                                    border_radius=ft.border_radius.all(10),
                                    src=f"assets/images/cards/tickets.png"
                                )
                            ]
                        )
                    ),
                    #  ----------for the top header text----------------//
                    ft.Container(
                        margin=ft.margin.only(left=20),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "tickets".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    font_family="Raleway-bold",
                                    size=30,
                                    color="#0078D9"
                                )
                            ]
                        )
                    ),
                    #  -------------// for the text here---------------//
                    ft.Container(
                        margin=ft.margin.only(left=20, top=10),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Welcome to the Tickets section,"
                                    " your gateway to an unforgettable experience. "
                                    "We're thrilled to offer you a hassle-free way "
                                    "to secure your tickets for our upcoming event."
                                    " Whether it's a concert, a conference, a sports"
                                    " game, or a special gathering, we've got you covered.",
                                    color="black",
                                    size=18,

                                )
                            ]
                        )
                    ),
                    #  ----------for the payment methods here----------------//
                    ft.Container(
                        margin=ft.margin.only(left=20),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "why choose us for your tickets".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    font_family="Raleway-bold",
                                    size=30,
                                    color="#0078D9"
                                )
                            ]
                        )
                    ),
                    #  ---------------// payment methods integration---------------//
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                #  ------// the first payment method---------//
                                ft.Container(
                                    margin=ft.margin.only(left=20, top=10),
                                    content=ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                elevation=None,
                                                width=200,
                                                height=70,
                                                icon=ft.icons.AIRPLANE_TICKET_ROUNDED,
                                                icon_color="white",
                                                color="white",
                                                text="tickets".capitalize(),
                                                bgcolor="#0078D9",
                                            )
                                        ]
                                    )
                                )
                                #  --------------// the second payment method------//
                            ]
                        )
                    )

                ]
            )
        )
    )

    #  ------------------------// function to open the streams page here---------//
    def open_streams_page_func(e):
        """the function will open the streams page here"""
        try:
            page.go("/streams")
            streaming_modal.open = False
            page.update()
        except Exception as ex:
            print(ex)

    #  ------------------streaming modal----------//
    streaming_modal = ft.AlertDialog(
        content=ft.Container(
            width=700,
            height=600,
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    #  -------------// the container for the image here--------//
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    width=700,
                                    height=300,
                                    border_radius=ft.border_radius.all(10),
                                    src=f"assets/images/cards/podcast.png"
                                )
                            ]
                        )
                    ),
                    #  ----------for the top header text----------------//
                    ft.Container(
                        margin=ft.margin.only(left=20),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "streaming".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    font_family="Raleway-bold",
                                    size=30,
                                    color="#0078D9"
                                )
                            ]
                        )
                    ),
                    #  -------------// for the text here---------------//
                    ft.Container(
                        margin=ft.margin.only(left=20, top=10),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "In today's fast-paced digital world, "
                                    "streaming is the go-to method for delivering"
                                    " content to your audience in real-time. Whether "
                                    "you're a content creator, a business owner, or an"
                                    " organization looking to reach a global audience, "
                                    "our streaming solutions provide a reliable and efficient"
                                    " way to engage your viewers.",
                                    color="black",
                                    size=18,

                                )
                            ]
                        )
                    ),
                    #  ----------for the payment methods here----------------//
                    ft.Container(
                        margin=ft.margin.only(left=20),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "streaming".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    font_family="Raleway-bold",
                                    size=30,
                                    color="#0078D9"
                                )
                            ]
                        )
                    ),
                    #  ---------------// payment methods integration---------------//
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                #  ------// the first payment method---------//
                                ft.Container(
                                    margin=ft.margin.only(left=20, top=10),
                                    content=ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                elevation=None,
                                                width=200,
                                                height=70,
                                                icon=ft.icons.STREAM_ROUNDED,
                                                icon_color="white",
                                                color="white",
                                                text="tickets".capitalize(),
                                                bgcolor="#0078D9",
                                                on_click=open_streams_page_func
                                            )
                                        ]
                                    )
                                )
                                #  --------------// the second payment method------//
                            ]
                        )
                    )

                ]
            )
        )
    )

    #  --------------// functions to trigger the modals here----------//
    def open_payment_modal(e):
        """the function will open up the payment modal"""
        try:
            page.dialog = payments_modal
            payments_modal.open = True
            page.update()
        except Exception as ex:
            print(ex)

    #  -----------------// function to open up the ticket modal here-------------//
    def open_tickes_modal(e):
        """the function will open the tickets modal"""
        try:
            page.dialog = tickets_modal
            tickets_modal.open = True
            page.update()
        except Exception as ex:
            print(ex)

    #  -----------------// the function to trigger the streaming method here----------//
    def open_streaming_modal(e):
        """the function will open the streaming modal"""
        try:
            page.dialog = streaming_modal
            streaming_modal.open = True
            page.update()
        except Exception as ex:
            print(ex)

    #  -----------------// the containers to be filled in the responsive rows-----//
    content = ft.ListView(
        expand=1,
        auto_scroll=True,
        spacing=10,
        height=800,
        scale=1.0,
        controls=[
            #  ---------------// the top most container for the website will be here-----//
            ft.Container(
                content=ft.Column(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        #  ----------------// the top container here---------------//
                        ft.Container(
                            margin=ft.margin.only(left=30, top=10),
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "malawi entertainers".capitalize(),
                                        font_family="Raleway",
                                        size=40,
                                        weight=ft.FontWeight.BOLD

                                    )
                                ]
                            )
                        ),
                        #  -----------------------/the container that wraps both columns here/---------------//
                        ft.Container(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Container(
                                        width=800,
                                        height=400,
                                        border_radius=ft.border_radius.all(10),
                                        margin=ft.margin.only(left=20, top=20),
                                        shadow=ft.BoxShadow(
                                            blur_radius=9,
                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                            color="#0050C1",
                                        ),
                                        gradient=ft.LinearGradient(
                                            colors=[
                                                "#311B92",
                                                "#0078D9",
                                            ],
                                            begin=ft.alignment.top_left,
                                            end=ft.alignment.top_right,
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                #  ---------------the top most text for the home page--//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, top=50),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.Text(
                                                                "home".capitalize(),
                                                                style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                                                color="white",
                                                                size=24,
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -------------------// container for the welcome information--------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, top=30),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.Container(
                                                                width=400,
                                                                content=ft.Column(
                                                                    controls=[
                                                                        ft.Text(
                                                                            "what's trending in \nentertainment",
                                                                            style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                                                            color="white",
                                                                            text_align=ft.alignment.center,
                                                                            font_family="Raleway"
                                                                        ),
                                                                        ft.Text(
                                                                            "get all the latest news \nand updates",
                                                                            color=ft.colors.GREY_50,
                                                                            size=20,
                                                                            font_family="Raleway"
                                                                        ),
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  ----------------// container for the button here------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=30, top=5),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.ElevatedButton(
                                                                width=200,
                                                                height=60,
                                                                icon=ft.icons.DETAILS_ROUNDED,
                                                                text="see details"
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  --------------------// the container for the image here---------//
                                    ft.Container(
                                        width=300,
                                        height=400,
                                        margin=ft.margin.only(right=100),
                                        content=ft.Row(
                                            controls=[
                                                ft.Image(
                                                    src="assets/stickers/people.png",
                                                    height=300,
                                                    width=300
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        #   --------------// the container that will hold all the top features-----------//
                        ft.Container(
                            margin=ft.margin.only(bottom=20),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    #  -----------// the first card for the
                                    ft.Container(
                                        margin=ft.margin.only(top=20),
                                        content=ft.Text(
                                            "our features".capitalize(),
                                            font_family="Raleway",
                                            size=30,
                                            color="#212121",
                                            weight=ft.FontWeight.W_700
                                        )
                                    ),

                                ]
                            )
                        ),
                        #  --------------// the section for the features page will be here----------//
                        ft.Container(
                            margin=ft.margin.only(bottom=300),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    #  ---------------// the first card for the site will be here-----//
                                    ft.Container(
                                        height=400,
                                        width=350,
                                        bgcolor=ft.colors.BLUE_GREY_900,
                                        border_radius=ft.border_radius.all(10),
                                        content=ft.Column(
                                            controls=[
                                                #  -------------// the container for the top icon---------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=30),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                ft.icons.PAYMENT_ROUNDED,
                                                                size=70,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  --------------// container for the text---------------//
                                                ft.Container(
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                "payments".capitalize(),
                                                                font_family="Raleway-bold",
                                                                size=24,
                                                                color="white",
                                                                weight=ft.FontWeight.W_700
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  ----------// container for the introductory text--------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=10, right=10),
                                                    content=ft.Column(
                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                        controls=[
                                                            ft.Text(
                                                                "provide a some text and the system will "
                                                                "automatically translate basing on the"
                                                                "topic that you have provide using, machine"
                                                                "learning and natural language"
                                                                "processing. the content generated is "
                                                                "proven to be of higher accuracy".title(),
                                                                weight=ft.FontWeight.W_500,
                                                                size=18,
                                                                color="white",
                                                                text_align=ft.alignment.center,
                                                                font_family="Raleway"
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                #  -------------------// button control-------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=10),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.OutlinedButton(
                                                                icon_color="white",
                                                                text="read more",
                                                                icon=ft.icons.MORE_ROUNDED,
                                                                on_click=open_payment_modal,
                                                                style=ft.ButtonStyle(
                                                                    color="white",
                                                                    shadow_color="white",
                                                                ),
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  ----------------//-----------------//-----------------//
                                    ft.Container(
                                        height=400,
                                        width=350,
                                        bgcolor=ft.colors.BLUE_GREY_900,
                                        border_radius=ft.border_radius.all(10),
                                        content=ft.Column(
                                            controls=[
                                                #  -------------// the container for the top icon---------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=30),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                ft.icons.BOOKMARK_BORDER_ROUNDED,
                                                                size=70,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  --------------// container for the text---------------//
                                                ft.Container(
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                "tickets".capitalize(),
                                                                font_family="Raleway-bold",
                                                                size=24,
                                                                color="white",
                                                                weight=ft.FontWeight.W_700
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  ----------// container for the introductory text--------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=10, right=10),
                                                    content=ft.Column(
                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                        controls=[
                                                            ft.Text(
                                                                "provide a some text and the system will "
                                                                "automatically translate basing on the"
                                                                "topic that you have provide using, machine"
                                                                "learning and natural language"
                                                                "processing. the content generated is "
                                                                "proven to be of higher accuracy".title(),
                                                                weight=ft.FontWeight.W_500,
                                                                size=18,
                                                                color="white",
                                                                text_align=ft.alignment.center,
                                                                font_family="Raleway"
                                                            ),

                                                        ]
                                                    )
                                                ),
                                                #  -------------------// button control-------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=10),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.OutlinedButton(
                                                                icon_color="white",
                                                                text="read more",
                                                                icon=ft.icons.MORE_ROUNDED,
                                                                on_click=open_tickes_modal,
                                                                style=ft.ButtonStyle(
                                                                    color="white",
                                                                    shadow_color="white",
                                                                ),
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  ----------------------//---------------------//
                                    ft.Container(
                                        height=400,
                                        width=350,
                                        bgcolor=ft.colors.BLUE_GREY_900,
                                        border_radius=ft.border_radius.all(10),
                                        content=ft.Column(
                                            controls=[
                                                #  -------------// the container for the top icon---------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=30),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                ft.icons.STREAM_ROUNDED,
                                                                size=70,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  --------------// container for the text---------------//
                                                ft.Container(
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                "streaming".capitalize(),
                                                                font_family="Raleway-bold",
                                                                size=24,
                                                                color="white",
                                                                weight=ft.FontWeight.W_700
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  ----------// container for the introductory text--------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=10, right=10),
                                                    content=ft.Column(
                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                        controls=[
                                                            ft.Text(
                                                                "provide a some text and the system will "
                                                                "automatically translate basing on the"
                                                                "topic that you have provide using, machine"
                                                                "learning and natural language"
                                                                "processing. the content generated is "
                                                                "proven to be of higher accuracy".title(),
                                                                weight=ft.FontWeight.W_500,
                                                                size=18,
                                                                color="white",
                                                                text_align=ft.alignment.center,
                                                                font_family="Raleway"
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                #  -------------------// button control-------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=10),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.OutlinedButton(
                                                                icon_color="white",
                                                                text="go to streams".capitalize(),
                                                                icon=ft.icons.STREAM_ROUNDED,
                                                                on_click=open_streaming_modal,
                                                                style=ft.ButtonStyle(
                                                                    color="white",
                                                                    shadow_color="white",
                                                                ),
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  ------------------------------------//-------------------//
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    )
    #  --------------------// functions to control the modals--------------//

    return content
