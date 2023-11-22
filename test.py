import flet as ft
import stripe
import qrcode
from Classes.payments import Payment

# Set your Stripe API keys
stripe.api_key = 'sk_test_51M3Ja4CS2j2b9xFxwTMUlfxDbOMNg9rvkKtCHNMP0uFAYl8PvYh9RrkzIZiOvBZlPjswqyP1Md81GWWQTkI9tDdK001WK9hZ2F'  # Replace with your Secret API Key


class PaymentView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        page.spacing = 0
        page.margin = 0
        #  ----------------// getting card payment amount here----------//
        self.amount = ft.TextField(
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
            value="89384",
        )
        #  ----------------------//---------------------------//
        self.gold_amount = ft.TextField(
            width=300,
            height=90,
            helper_text="enter your amount",
            hint_text="gold amount",
            tooltip="start payments".capitalize(),
            prefix_icon=ft.icons.PAYMENT_ROUNDED,
            border_color="#311B92",
            autofocus=True,
            read_only=True,
            text_size=24,
            animate_size=True,
            value="7847",
        )
        #  -------------------//-------------------//
        self.silver_amount = ft.TextField(
            width=300,
            height=90,
            helper_text="enter your amount",
            hint_text="gold amount",
            tooltip="start payments".capitalize(),
            prefix_icon=ft.icons.PAYMENT_ROUNDED,
            border_color="#311B92",
            autofocus=True,
            read_only=True,
            text_size=24,
            animate_size=True,
            value="643",
        )
        #  ----------------// the drop down for the current here--------------//
        self.currency = ft.Dropdown(
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
            options=[
                ft.dropdown.Option("kwacha".capitalize()),
                ft.dropdown.Option("Dollar".capitalize()),
            ]
        )
        #  -----------------//----------------------//----------------------//------------//
        self.source = ft.TextField(
            width=300,
            height=90,
            helper_text="enter your card token",
            hint_text="card token",
            tooltip="visa card token".capitalize(),
            prefix_icon=ft.icons.TOKEN_ROUNDED,
            border_color="#311B92",
            autofocus=True,
            text_size=24,
            animate_size=True,
        )

        #  ------------------// the description for the payment-----------------//
        self.description = ft.TextField(
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
        )
        #  ----------------// the custom fonts for the website will be here for the imports here----//
        self.page.fonts = {
            "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
            "Raleway": "assets/fonts/static/Raleway-Light.ttf",
            "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
            "Roboto-black": "assets/fonts/Roboto-Black.ttf",
            "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
        }
        #  ------------// the dialog for the payment details here----------//
        self.payment_modal = ft.AlertDialog(
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
                                        "buy diamond ticket".capitalize(),
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
                                    ft.Row([self.amount, self.currency]),
                                    ft.Row([self.source, self.description]),
                                    ft.Container(
                                        margin=ft.margin.only(top=10, bottom=20),
                                        content=ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    width=200,
                                                    height=60,
                                                    on_click=self.validate_input_func,
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
        #  --------------------// alert dialog for the diamond ticket here--------//
        self.payment_gold_modal = ft.AlertDialog(
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
                                        "buy gold ticket".capitalize(),
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
                                        src="assets/stickers/circus.png",
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
                                    ft.Row([self.gold_amount, self.currency]),
                                    ft.Row([self.source, self.description]),
                                    ft.Container(
                                        margin=ft.margin.only(top=10, bottom=20),
                                        content=ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    width=200,
                                                    height=60,
                                                    on_click=self.validate_input_func,
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
        #  -------------------// alert dialog for the silver ticket------------//
        self.payment_silver_modal = ft.AlertDialog(
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
                                        "buy silver ticket".capitalize(),
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
                                        src="assets/stickers/ticket (1).png",
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
                                    ft.Row([self.silver_amount, self.currency]),
                                    ft.Row([self.source, self.description]),
                                    ft.Container(
                                        margin=ft.margin.only(top=10, bottom=20),
                                        content=ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    width=200,
                                                    height=60,
                                                    on_click=self.validate_input_func,
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

    #  ------------------// validating input fields-----------------//
    def validate_input_func(self, e):
        try:
            if not self.amount.value:
                self.amount.error_text = "make sure to add amount".capitalize()
                self.page.update()
            elif not self.currency.value:
                self.currency.error_text = "select currency first".capitalize()
                self.page.update()
            elif not self.source.value:
                self.source.error_text = "select card source".capitalize()
                self.page.update()
            elif not self.description.value:
                self.description.error_text = "add something".capitalize()
                self.page.update()
            else:
                self.process_valid_payments_func()
                self.save_payment_details_db()
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

    #  -------------// functions will start here------//
    def open_payment_modal_func(self, e):
        """function to open the payment modal here"""
        try:
            self.page.dialog = self.payment_modal
            self.payment_modal.open = True
            self.page.update()
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
            self.page.update()

    #  ----------------// function to open the gold modal here----------//
    def open_silver_modal(self, e):
        try:
            self.page.dialog = self.payment_silver_modal
            self.payment_silver_modal.open = True
            self.page.update()
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
            self.page.update()

    #  ----------------------// function will open the gold modal
    def open_gold_modal(self, e):
        try:
            self.page.dialog = self.payment_gold_modal
            self.payment_gold_modal.open = True
            self.page.update()
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
            self.page.update()

    #  ----------------------function to process the payments here--------------//
    def process_valid_payments_func(self):
        # Set your Stripe secret key
        stripe.api_key = 'sk_test_51M3Ja4CS2j2b9xFxwTMUlfxDbOMNg9rvkKtCHNMP0uFAYl8PvYh9RrkzIZiOvBZlPjswqyP1Md81GWWQTkI9tDdK001WK9hZ2F'

        # Create a charge
        try:
            charge = stripe.Charge.create(
                amount=self.amount.value,  # Amount in cents
                currency='usd',
                source='tok_visa',  # Replace with a valid token or card ID
                description=self.description.value,
                receipt_email="martinsilungwe12@gmail.com"
            )
            # Charge was successful
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "your payment was processed successfully with the ID".format(charge.id)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.dialog = self.payment_modal
            self.payment_modal.open = False
            self.page.update()

        except stripe.error.CardError as e:
            # Card was declined
            error_info = e.json_body
            err_message = error_info['error']['message']
            print("Card was declined:", err_message)

        except Exception as e:
            # Other errors
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#b71c1c",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "please check your account number and try again".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.payment_modal.open = False
            self.page.update()

    #  -------------------//-------------------------//
    def generate_diamond_code(self):
        # Data to be encoded in the QR code
        data = "Hello, QR Code!"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=200,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="#E52E6A", back_color="white")

        # Save the image or display it
        img.save("assets/images/diamond/qrcode.png")

    #  ---------------// function for generating the qr codes here---------//
    def generate_diamond_qr_func(self, e):
        try:
            #  ----------------// the payment QR codes will be here-------//
            diamond_qr_code_modal = ft.AlertDialog(
                content=ft.Container(
                    width=500,
                    bgcolor="white",
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Icon(
                                            ft.icons.QR_CODE_ROUNDED,
                                            color=ft.colors.BLACK,
                                            size=70,
                                        )
                                    ]
                                )
                            ),
                            #  ----------------//-------------------//
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "scan qr code",
                                            style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                            color="blue",
                                            font_family="Raleway-bold"
                                        )
                                    ]
                                )
                            ),
                            # ------------------// generated code will be here------//
                            ft.Container(
                                height=400,
                                width=500,
                                margin=ft.margin.only(top=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src="assets/images/diamond/qrcode.png",
                                            border_radius=ft.border_radius.all(10)
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
            self.page.dialog = diamond_qr_code_modal
            diamond_qr_code_modal.open = True
            self.page.update()
            self.generate_diamond_code()
        except Exception as ex:
            print(ex)

    #  ---------------------// function to generate gold qr codes here--------//
    def generate_gold_code(self):
        # Data to be encoded in the QR code
        data = "gold qr code"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=200,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="#FFB84A", back_color="white")

        # Save the image or display it
        img.save("assets/images/gold/qrcode.png")

    def generate_gold_qr_func(self, e):
        try:
            #  ----------------// the payment QR codes will be here-------//
            diamond_qr_code_modal = ft.AlertDialog(
                content=ft.Container(
                    width=500,
                    bgcolor="white",
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Icon(
                                            ft.icons.QR_CODE_ROUNDED,
                                            color=ft.colors.BLACK,
                                            size=70,
                                        )
                                    ]
                                )
                            ),
                            #  ----------------//-------------------//
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "scan qr code",
                                            style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                            color="blue",
                                            font_family="Raleway-bold"
                                        )
                                    ]
                                )
                            ),
                            # ------------------// generated code will be here------//
                            ft.Container(
                                height=400,
                                width=500,
                                margin=ft.margin.only(top=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src="assets/images/gold/qrcode.png",
                                            border_radius=ft.border_radius.all(10)
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
            self.page.dialog = diamond_qr_code_modal
            diamond_qr_code_modal.open = True
            self.page.update()
            self.generate_gold_code()
        except Exception as ex:
            print(ex)

    #  --------------------// function to generate silver tickets here-----------//
    #  ---------------------// function to generate gold qr codes here--------//
    def generate_silver_code(self):
        # Data to be encoded in the QR code
        data = "gold qr code"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=200,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="#6C5B8B", back_color="white")

        # Save the image or display it
        img.save("assets/images/silver/qrcode.png")

    def generate_silver_qr_func(self, e):
        try:
            #  ----------------// the payment QR codes will be here-------//
            diamond_qr_code_modal = ft.AlertDialog(
                content=ft.Container(
                    width=500,
                    bgcolor="white",
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Icon(
                                            ft.icons.QR_CODE_ROUNDED,
                                            color=ft.colors.BLACK,
                                            size=70,
                                        )
                                    ]
                                )
                            ),
                            #  ----------------//-------------------//
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "scan qr code",
                                            style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                            color="blue",
                                            font_family="Raleway-bold"
                                        )
                                    ]
                                )
                            ),
                            # ------------------// generated code will be here------//
                            ft.Container(
                                height=400,
                                width=500,
                                margin=ft.margin.only(top=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src="assets/images/silver/qrcode.png",
                                            border_radius=ft.border_radius.all(10)
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
            self.page.dialog = diamond_qr_code_modal
            diamond_qr_code_modal.open = True
            self.page.update()
            self.generate_silver_code()
        except Exception as ex:
            print(ex)

    #  ------------------// function for the chips here------------//

    def build(self):
        return ft.ListView(
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
                                                                    on_click=self.open_payment_modal_func,
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
                                                                    on_click=self.generate_diamond_qr_func,
                                                                    autofocus=True,
                                                                    color="white",
                                                                    bgcolor="#E52E6A",
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
                                                                    on_click=self.open_gold_modal,
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
                                                                    on_click=self.generate_gold_qr_func,
                                                                    autofocus=True,
                                                                    color="white",
                                                                    bgcolor="#FF7451",
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
                                                                    on_click=self.open_silver_modal,
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
                                                                    on_click=self.generate_silver_qr_func,
                                                                    autofocus=True,
                                                                    color="white",
                                                                    bgcolor="#0050C1",
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

    #  ----------------// function to save the payment details-------//
    def save_payment_details_db(self):
        try:
            payment = Payment(
                self.amount.value,
                self.currency.value,
                self.source.value,
                self.description.value
            )
            payment.save_payment_details_func()
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
