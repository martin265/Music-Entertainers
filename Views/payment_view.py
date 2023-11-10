import flet as ft
import stripe

# Set your Stripe API keys
stripe.api_key = 'sk_test_51M3Ja4CS2j2b9xFxwTMUlfxDbOMNg9rvkKtCHNMP0uFAYl8PvYh9RrkzIZiOvBZlPjswqyP1Md81GWWQTkI9tDdK001WK9hZ2F'  # Replace with your Secret API Key


def PaymentView(page):
    page.spacing = 0
    page.margin = 0

    amount = ft.TextField(
        width=300,
        height=90,
        helper_text="enter your amount",
        hint_text="amount",
        tooltip="start payments".capitalize(),
        prefix_icon=ft.icons.PAYMENT_ROUNDED,
        border_color="#311B92",
        autofocus=True,
        read_only=True,
        text_size=24,
        animate_size=True,
        value="557",
        border_radius=ft.border_radius.all(10)
    )
    #  ----------------// the drop down for the current here--------------//
    currency = ft.Dropdown(
        width=300,
        height=90,
        helper_text="select currency",
        hint_text="currency",
        tooltip="check your currency".capitalize(),
        prefix_icon=ft.icons.CURRENCY_BITCOIN_ROUNDED,
        border_color="#311B92",
        autofocus=True,
        text_size=24,
        animate_size=True,
        value="k557",
        border_radius=ft.border_radius.all(10),
        options=[
            ft.dropdown.Option("usd")
        ]
    )
    #  -----------------//----------------------//----------------------//------------//
    source = ft.Dropdown(
        width=300,
        height=90,
        helper_text="select payment source",
        hint_text="source",
        tooltip="check your source".capitalize(),
        prefix_icon=ft.icons.SOURCE_ROUNDED,
        border_color="#311B92",
        autofocus=True,
        text_size=24,
        animate_size=True,
        border_radius=ft.border_radius.all(10),
        options=[
            ft.dropdown.Option("tok visa".capitalize())
        ]
    )
    #  ------------------// the description for the payment-----------------//
    description = ft.TextField(
        width=300,
        height=90,
        helper_text="enter your description",
        hint_text="description",
        tooltip="say something".capitalize(),
        prefix_icon=ft.icons.DESCRIPTION_ROUNDED,
        border_color="#311B92",
        autofocus=True,
        text_size=24,
        animate_size=True,
        multiline=True,
        border_radius=ft.border_radius.all(10)
    )
    #  ----------------// the custom fonts for the website will be here for the imports here----//
    page.fonts = {
        "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
        "Raleway": "assets/fonts/static/Raleway-Light.ttf",
        "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
        "Roboto-black": "assets/fonts/Roboto-Black.ttf",
        "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
    }

    #  ------------------// validating input fields-----------------//
    def validate_input_func(e):
        try:
            if not amount.value:
                amount.error_text = "make sure to add amount".capitalize()
                page.update()
            elif not currency.value:
                currency.error_text = "select currency first".capitalize()
                page.update()
            elif not source.value:
                source.error_text = "select card source".capitalize()
                page.update()
            elif not description.value:
                description.error_text = "add something".capitalize()
                page.update()
            else:
                process_valid_payments_func()
                print("zitheka koma")
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()

    #  ------------// the dialog for the payment details here----------//
    payment_modal = ft.AlertDialog(
        content=ft.Container(
            bgcolor="white",
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(
                blur_radius=6,
                blur_style=ft.ShadowBlurStyle.OUTER,
                color="white",
            ),
            width=700,
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    #  ----------// the top text for the modal here------//
                    ft.Container(
                        margin=ft.margin.only(top=30),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "diamond ticket".capitalize(),
                                    style=ft.TextThemeStyle.DISPLAY_SMALL,
                                    color="#311B92"
                                )
                            ]
                        )
                    ),
                    #  --------------// the container for the sample text here----//
                    ft.Container(
                        margin=ft.margin.only(top=20),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Image(
                                    src="assets/stickers/ticket.png",
                                    height=100,
                                    width=100,
                                )
                            ]
                        )
                    ),
                    #  -------------// container for the bottom text heere-----//
                    ft.Container(
                        margin=ft.margin.only(left=40, right=40, top=20),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    wrap=True,
                                    controls=[
                                        ft.Text(
                                            "At Music Entertainers we take the security of your payment "
                                            "information and personal data seriously. We are committed "
                                            "to ensuring a safe and secure environment for all transactions.",
                                            color="#212121",
                                            text_align=ft.alignment.center,
                                            font_family="Raleway",
                                            size=20,
                                            weight=ft.FontWeight.W_300,
                                            no_wrap=False,
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    #  ---------------// container for the input controls----------//
                    ft.Container(
                        margin=ft.margin.only(left=30, right=30, top=20),
                        content=ft.Column(
                            controls=[
                                ft.Row([amount, currency]),
                                ft.Row([source, description]),
                                ft.Container(
                                    margin=ft.margin.only(top=10, bottom=20),
                                    content=ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                width=200,
                                                height=60,
                                                on_click=validate_input_func,
                                                autofocus=True,
                                                color="white",
                                                bgcolor="#0050C1",
                                                elevation=None,
                                                icon=ft.icons.PAYPAL_ROUNDED,
                                                text="pay for ticket".capitalize(),
                                                tooltip="pay ticket".capitalize()
                                            )
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

    #  -------------// functions will start here------//
    def open_payment_modal_func(e):
        """function to open the payment modal here"""
        try:
            page.dialog = payment_modal
            payment_modal.open = True
            page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.update()

    #  ----------------------function to process the payments here--------------//
    def process_valid_payments_func():
        # Set your Stripe secret key
        stripe.api_key = 'sk_test_51M3Ja4CS2j2b9xFxwTMUlfxDbOMNg9rvkKtCHNMP0uFAYl8PvYh9RrkzIZiOvBZlPjswqyP1Md81GWWQTkI9tDdK001WK9hZ2F'

        # Create a charge
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency='usd',
                source='tok_visa',  # Replace with a valid token or card ID
                description='Example charge',
            )
            # Charge was successful
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "your payment was processed successfully with the ID".format(charge.id)
                        )
                    ]
                )
            )
            page.dialog = payment_modal
            payment_modal.open = False
            page.update()

        except stripe.error.CardError as e:
            # Card was declined
            error_info = e.json_body
            err_message = error_info['error']['message']
            print("Card was declined:", err_message)

        except Exception as e:
            # Other errors
            print("An error occurred:", str(e))

    #  -----// returning the content here
    content = ft.ListView(
        expand=1,
        auto_scroll=True,
        spacing=10,
        height=800,
        scale=1.0,
        controls=[
            #  ---------// the main container here--------//
            ft.Container(
                content=ft.Column(
                    controls=[
                        #  -------------// container for the top text here---------//
                        ft.Container(
                            margin=ft.margin.only(top=40),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "payment gateway".capitalize(),
                                        font_family="Raleway-bold",
                                        size=24,
                                        style=ft.TextThemeStyle.DISPLAY_SMALL,
                                        color="#311B92"
                                    )
                                ]
                            )
                        ),
                        #  ---------------// container for the text here----------//
                        ft.Container(
                            margin=ft.margin.only(top=30),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        height=500,
                                        width=400,
                                        border_radius=ft.border_radius.all(10),
                                        gradient=ft.LinearGradient(
                                            colors=[
                                                "#4A148C",
                                                "#673AB7"
                                            ],

                                        ),
                                        shadow=ft.BoxShadow(
                                            blur_radius=9,
                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                            color="#311B92",
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                #  -----// container for the icon here-----//
                                                ft.Container(
                                                    margin=ft.margin.only(top=20),
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
                                                #  -------// for the text here--------//
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
                                                #  -----------// container for the main information-------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, right=20, top=10),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Text(
                                                                "Premium Seating: Diamond ticket holders"
                                                                " often enjoy better seating arrangements"
                                                                " with improved views of the event, whether"
                                                                " it's a concert, sports game,"
                                                                " or theater performa",
                                                                color="white",
                                                                font_family="Raleway",
                                                                size=20
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  ------------------// container for the buttons------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, top=40),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.OutlinedButton(
                                                                width=200,
                                                                height=60,
                                                                text="check out payment".capitalize(),
                                                                on_click=open_payment_modal_func,
                                                                icon=ft.icons.CHECK_ROUNDED,
                                                                autofocus=True,
                                                                tooltip="check out payments".capitalize(),
                                                                style=ft.ButtonStyle(
                                                                    color="white",
                                                                    animation_duration=400,
                                                                )
                                                            ),
                                                            #  -------------// the button for the booking------//
                                                            ft.ElevatedButton(
                                                                width=150,
                                                                height=60,
                                                                on_click={},
                                                                autofocus=True,
                                                                color="white",
                                                                bgcolor="#E52E6A",
                                                                elevation=None,
                                                                icon=ft.icons.SCHEDULE_ROUNDED,
                                                                text="schedule".capitalize(),
                                                                tooltip="schedule your ticket".capitalize()
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  ----------------// the second card for the ticket payment--------//
                                    ft.Container(
                                        height=500,
                                        width=400,
                                        border_radius=ft.border_radius.all(10),
                                        gradient=ft.LinearGradient(
                                            colors=[
                                                "#4A148C",
                                                "#673AB7"
                                            ],

                                        ),
                                        shadow=ft.BoxShadow(
                                            blur_radius=9,
                                            blur_style=ft.ShadowBlurStyle.NORMAL,
                                            color="#311B92",
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                #  -----// container for the icon here-----//
                                                ft.Container(
                                                    margin=ft.margin.only(top=20),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                ft.icons.MONEY_ROUNDED,
                                                                size=100,
                                                                color="#FFC052"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -------// for the text here--------//
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
                                                #  -------------------//-------------------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, right=20, top=10),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Text(
                                                                "Premium Seating: Gold ticket holders"
                                                                " often enjoy better seating arrangements"
                                                                " with improved views of the event, whether"
                                                                " it's a concert, sports game,"
                                                                " or theater performa",
                                                                color="white",
                                                                font_family="Raleway",
                                                                size=20
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -------------------//----------------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, top=40),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.OutlinedButton(
                                                                width=200,
                                                                height=60,
                                                                text="check out payment".capitalize(),
                                                                on_click={},
                                                                icon=ft.icons.CHECK_ROUNDED,
                                                                autofocus=True,
                                                                tooltip="check out payments".capitalize(),
                                                                style=ft.ButtonStyle(
                                                                    color="white",
                                                                    animation_duration=400,
                                                                )
                                                            ),
                                                            #  -------------// the button for the booking------//
                                                            ft.ElevatedButton(
                                                                width=150,
                                                                height=60,
                                                                on_click={},
                                                                autofocus=True,
                                                                color="white",
                                                                bgcolor="#FF7451",
                                                                elevation=None,
                                                                icon=ft.icons.SCHEDULE_ROUNDED,
                                                                text="schedule".capitalize(),
                                                                tooltip="schedule your ticket".capitalize()
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  ---------------------// the second container will be here for the tickets----------//
                                    ft.Container(
                                        height=500,
                                        width=400,
                                        border_radius=ft.border_radius.all(10),
                                        gradient=ft.LinearGradient(
                                            colors=[
                                                "#4A148C",
                                                "#673AB7"
                                            ],

                                        ),
                                        shadow=ft.BoxShadow(
                                            blur_radius=9,
                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                            color="#311B92",
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                #  -----// container for the icon here-----//
                                                ft.Container(
                                                    margin=ft.margin.only(top=20),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                ft.icons.STAR_OUTLINED,
                                                                size=100,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -------// for the text here--------//
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
                                                #  -------------------//-----------------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, right=20, top=10),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Text(
                                                                "Premium Seating: Silver ticket holders"
                                                                " often enjoy better seating arrangements"
                                                                " with improved views of the event, whether"
                                                                " it's a concert, sports game,"
                                                                " or theater performa",
                                                                color="white",
                                                                font_family="Raleway",
                                                                size=20
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -----------------//-----------------------------//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, top=40),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.OutlinedButton(
                                                                width=200,
                                                                height=60,
                                                                text="check out payment".capitalize(),
                                                                on_click={},
                                                                icon=ft.icons.CHECK_ROUNDED,
                                                                autofocus=True,
                                                                tooltip="check out payments".capitalize(),
                                                                style=ft.ButtonStyle(
                                                                    color="white",
                                                                    animation_duration=400,
                                                                )
                                                            ),
                                                            #  -------------// the button for the booking------//
                                                            ft.ElevatedButton(
                                                                width=150,
                                                                height=60,
                                                                on_click={},
                                                                autofocus=True,
                                                                color="white",
                                                                bgcolor="#0050C1",
                                                                elevation=None,
                                                                icon=ft.icons.SCHEDULE_ROUNDED,
                                                                text="schedule".capitalize(),
                                                                tooltip="schedule your ticket".capitalize()
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                    #  -------------------------//
                                ]
                            )

                        ),
                        #  ------------------// container for the scroll
                        ft.Container(
                            height=300,
                            margin=ft.margin.only(bottom=40, top=40)
                        )
                    ]
                )
            )
        ]
    )
    return content
