import flet as ft
from Classes.tracking import PaymentTracking
import datetime
import stripe
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class SendQrEmail(ft.UserControl):
    def __init__(self, page: ft.Page, sender_email, sender_password, recipient_email, subject, body, image_path):
        super().__init__()
        self.page = page
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body
        self.image_path = image_path

        # # Replace the following with your own information
        # self.sender_email = 'zaithwazonke@gmail.com'
        # self.sender_password = 'cihk icag tfgf zrob'
        # self.recipient_email = self.recipient_email
        # self.subject = self.subject
        # self.body = self.body
        # self.image_path = self.image_path

    #  ------------------// function will send the email attachments here //----------
    def send_email(self):
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.recipient_email
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, 'plain'))

        # Attach the image
        with open(self.image_path, 'rb') as attachment:
            image_mime = MIMEImage(attachment.read(), _subtype="png")
            attachment.close()
            image_mime.add_header('Content-Disposition', 'attachment', filename=self.image_path)
            message.attach(image_mime)

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Log in to your Gmail account
        server.login(self.sender_email, self.sender_password)

        # Send the email
        server.sendmail(self.sender_email, self.recipient_email, message.as_string())

        # Quit the server
        server.quit()

    def build(self):
        return ft.ListView()


class SilverQrGenerator(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def generate_silver_code(self):
        # Data to be encoded in the QR code
        data = "silver ticket price is K1000"

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


class GoldQrGenerator(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def generate_gold_code(self):
        # Data to be encoded in the QR code
        data = "gold ticket price is K2000"

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

    def build(self):
        return ft.ListView()


class QrCodeGenerator(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    #  -----------------// function to get the qr codes here----------//
    def generate_diamond_code(self):
        # Data to be encoded in the QR code
        data = "diamond ticket price is K3000"

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

    def build(self):
        return ft.ListView()


class ClientDetails(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.dd = ft.Text()

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

        self.event_name = ft.Dropdown(
            width=480,
            height=100,
            prefix_icon=ft.icons.EVENT_NOTE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="event name".capitalize(),
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
                ft.dropdown.Option("Bash".capitalize()),
                ft.dropdown.Option("Dances".capitalize()),
                ft.dropdown.Option("Drinks and Rap"),
            ],
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
        self.current_ticket_price = ft.Text()

        self.sender_email = 'zaithwazonke@gmail.com'
        self.sender_password = 'cihk icag tfgf zrob'
        self.recipient_email = 'martinsilungwe12@gmail.com'
        self.subject = 'Ticket Qr Code'
        self.body = 'Scan Qr Code'
        self.image_path = "assets/images/gold/qrcode.png"

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

        #  ----------------// the objects for generating the qr codes here---------//
        self.qr_code_generator = QrCodeGenerator(page=page)

        self.gold_qr_generator = GoldQrGenerator(page=page)

        self.silver_qr_generator = SilverQrGenerator(page=page)

        #  ----------------------the object to send the email with the qr code //---------//

    def clicked(self, e):
        try:
            if self.client_details.ticket_type == "gold":
                self.payment_details.amount.value = 2000
                print("gold ticket selected")
            #  --------------------------//-----------------------//
            elif self.client_details.ticket_type == "silver":
                self.payment_details.amount.value = 1000

            #  --------------------//---------------------------//
            elif self.client_details.ticket_type == "diamond":
                self.payment_details.amount = 3000
            else:
                print("no available tickets")
        except Exception as ex:
            print(ex)

    def InitialisePaymentDetails(self, e):
        try:
            if not self.client_details.first_name.value:
                self.client_details.first_name.error_text = "fill in the blanks first".capitalize()
                self.update()
            elif not self.client_details.last_name.value:
                self.client_details.last_name.error_text = "fill in the blanks first".capitalize()
                self.update()

            elif not self.client_details.email.value:
                self.client_details.email.error_text = "enter your email".capitalize()
                self.update()

            elif not self.client_details.phone_number.value:
                self.client_details.phone_number.error_text = "fill your phone number".capitalize()
                self.update()

            elif not self.client_details.event_name.value:
                self.client_details.event_name.error_text = "select event name".capitalize()
                self.update()

            elif not self.client_details.ticket_type.value:
                self.client_details.ticket_type.error_text = "select ticket".capitalize()
                self.update()

            elif not self.payment_details.amount.value:
                self.payment_details.amount.error_text = "check payment".capitalize()
                self.update()

            elif not self.payment_details.currency.value:
                self.payment_details.currency = "select currency".capitalize()
                self.update()

            elif not self.payment_details.source.value:
                self.payment_details.source.error_text = "enter card toket".capitalize()
                self.update()

            else:
                self.save_payment_details_func()
                self.process_valid_payments()
                self.send_email_func()
        except Exception as ex:
            print(ex)

    def send_email_func(self):
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = self.recipient_email
            message['Subject'] = self.subject
            message.attach(MIMEText(self.body, 'plain'))

            # Attach the image
            with open(self.image_path, 'rb') as attachment:
                image_mime = MIMEImage(attachment.read(), _subtype="png")
                attachment.close()
                image_mime.add_header('Content-Disposition', 'attachment', filename=self.image_path)
                message.attach(image_mime)

            # Connect to the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Log in to your Gmail account
            server.login(self.sender_email, self.sender_password)

            # Send the email
            server.sendmail(self.sender_email, self.recipient_email, message.as_string())

            # Quit the server
            server.quit()
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "email sent successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    def save_payment_details_func(self):
        try:
            current_date = datetime.datetime.now().strftime("%d, %A, %B")
            payment_tracking = PaymentTracking(
                self.client_details.first_name.value,
                self.client_details.last_name.value,
                self.client_details.email.value,
                self.client_details.phone_number.value,
                self.client_details.event_name.value,
                self.client_details.ticket_type.value,
                self.payment_details.amount.value,
                self.payment_details.currency.value,
                self.payment_details.source.value,
                self.payment_details.cvv.value,
                self.payment_details.xpr.value,
                current_date
            )
            payment_tracking.save_payment_details()
            #  -----------------// snack bar for showing the success message //-------------//
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "payment details processed successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

        except Exception as ex:
            print(ex)

    def process_valid_payments(self):
        try:
            # Set your secret key
            stripe.api_key = "sk_test_51OFGafFuspposRdyZiOJojteaDcZnTVtiNdeXcifEkR4z2az10MAJtRWfHlvyEBygaYwo9CAecVLsB1nQ3NT4WYe00sokapQVl"

            # Create a customer
            customer = stripe.Customer.create(
                email="zaithwazonke@gmail.com",
                source="tok_visa"  # Use a test card token from Stripe
            )

            # Create a charge
            charge = stripe.Charge.create(
                amount=self.payment_details.amount.value,  # Amount in cents
                currency="usd",
                description="Example charge",
                customer=customer.id
            )

            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                f"payment details processed successfully with ID of {charge.id}".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong at {}".format(ex)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    def getting_valid_image(self):
        if self.client_details.ticket_type == "gold":
            self.image_path = "assets/images/gold/qrcode.png"

    def build(self):
        self.getting_valid_image()
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
                                                        on_click=self.qr_code_generator.generate_diamond_qr_func,
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
                                                        on_click=self.gold_qr_generator.generate_gold_qr_func,
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
                                                        on_click=self.silver_qr_generator.generate_silver_qr_func,
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
                #  //---------------------// footer //-----------------------//
                ft.Container(
                    height=200,
                    margin=ft.margin.only(top=40),
                    gradient=ft.LinearGradient(
                        colors=[
                            "#0078D9",
                            "#311B92",
                        ],
                        begin=ft.alignment.bottom_left,
                        end=ft.alignment.top_left,
                    ),
                    content=ft.Row(
                        controls=[

                        ]
                    )
                ),

                #  //---------------------// footer //-----------------------//
                ft.Container(
                    height=10,
                    content=ft.Row(
                        controls=[
                            
                        ]
                    )
                ),

            ]
        )
