import flet as ft
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Classes.clients import ContactUs


class ContactView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
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
        #  ----------------// the input fields for the collection here-------------//
        self.first_name = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter characters only".capitalize(),
            hint_text="first name".capitalize(),
            label="first name".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.PERSON_ROUNDED
        )
        #  ------------------//--------------------------------//
        self.last_name = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter characters only".capitalize(),
            hint_text="last name".capitalize(),
            label="last name".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.PERSON_ROUNDED
        )
        #  -------------------------//-----------------------------//
        self.email = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter characters only".capitalize(),
            hint_text="email".capitalize(),
            label="email".capitalize(),
            keyboard_type=ft.KeyboardType.EMAIL,
            prefix_icon=ft.icons.EMAIL_ROUNDED
        )
        # --------------------------//----------------------------//
        self.phone_number = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter numbers only".capitalize(),
            hint_text="phone number".capitalize(),
            label="phone number".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.PHONE_ANDROID_ROUNDED
        )
        #  -----------------------//------------------------------//
        self.event_name = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter characters only".capitalize(),
            hint_text="event name".capitalize(),
            label="event name".capitalize(),
            keyboard_type=ft.KeyboardType.TEXT,
            prefix_icon=ft.icons.EVENT_AVAILABLE_ROUNDED
        )
        #  ----------------------------//----------------------------//
        self.ordering_number = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter numbers only".capitalize(),
            hint_text="ordering".capitalize(),
            label="ordering number".capitalize(),
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.icons.NUMBERS_ROUNDED
        )
        #  ------------------------//--------------------------//
        self.inquiry = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            helper_text="enter characters only".capitalize(),
            hint_text="enter message".capitalize(),
            label="enter message".capitalize(),
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            keyboard_type=ft.KeyboardType.TEXT,
            multiline=True,
            max_lines=900
        )

    #  ------------------------------// function to validate the inputs here----------//
    def validate_contact_inputs(self, e):
        """the function to validate the user inputs"""
        try:
            if not self.first_name.value:
                self.first_name.error_text = "fill in the blanks".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            #  -------------------//----------------------------//
            elif not self.last_name.value:
                self.last_name.error_text = "enter your last name".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            #  -----------------------//------------------------//
            elif not self.email.value:
                self.email.error_text = "fill in the email address".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            #  --------------------------//--------------------------//
            elif not self.phone_number.value:
                self.phone_number.error_text = "enter your phone number".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            #  --------------------------------//--------------------//
            elif not self.event_name.value:
                self.event_name.error_text = "add an event first".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            #  -------------------------//-------------------------//
            elif not self.ordering_number.value:
                self.ordering_number.error_text = "enter the ordering number".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            #  ------------------------//----------------------------//
            elif not self.inquiry.value:
                self.inquiry.error_text = "type in some inquiry message".capitalize()
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                self.send_email_notification()
                self.save_contact_details_func()
        except Exception as e:
            print(e)

    #  --------------------// the function will send the email address to the clients-------//
    def send_email_notification(self):
        try:
            #  ---------------------// the codes for sending the email notifications here-----------//
            # Gmail account details
            sender_email = "zaithwazonke@gmail.com"
            sender_password = "cihk icag tfgf zrob"

            # Gmail SMTP server
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Email content
            subject = "Subject of the Email"
            recipient_email = self.email.value
            email_body = self.inquiry.value

            #  --------------// email structure here----------------//
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(email_body, "plain"))

            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)

            # Start TLS encryption for security
            server.starttls()

            # Log in to your Gmail account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())

            # Quit the SMTP server
            server.quit()
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#311B92",
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                "email sent successfully".capitalize(),
                                size=20,
                                color="white"
                            )
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

        except Exception as e:
            print(e)

    #  ------------------// the build function to the controls here-------//
    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                ft.Container(
                    content=ft.Column(
                        #  ----------------// the top container here------------//
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=20, bottom=20, left=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "contact us",
                                            font_family="Raleway-bold",
                                            size=24
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                margin=ft.margin.only(right=10, left=10, bottom=30),
                                bgcolor="white",
                                width=1300,
                                height=600,
                                shadow=ft.BoxShadow(
                                    blur_radius=9,
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                    color="#0050C1",
                                ),
                                #  --------------// the content page for the-------------//
                                content=ft.Row(
                                    controls=[
                                        #  ---------------// the container for the sticker------//
                                        ft.Container(
                                            width=400,
                                            content=ft.Row(
                                                controls=[
                                                    ft.Image(
                                                        src=f"assets/contact/registration.png"
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ------------------// the container for the form here-----//
                                        ft.Container(
                                            margin=ft.margin.only(top=30, left=60),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row([self.first_name, self.last_name]),
                                                    ft.Row([self.email, self.phone_number]),
                                                    ft.Row([self.event_name, self.ordering_number]),
                                                    ft.Row([self.inquiry]),
                                                    #  --------------//-------------//
                                                    ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.ElevatedButton(
                                                                    width=200,
                                                                    height=50,
                                                                    text="contact us".capitalize(),
                                                                    icon=ft.icons.PERM_CONTACT_CALENDAR_ROUNDED,
                                                                    on_click=self.validate_contact_inputs,
                                                                    elevation=None,
                                                                    bgcolor="#0078D9",
                                                                    color="white"
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
                            #  -------------------//-----------------------//
                            ft.Container(
                                margin=ft.margin.only(top=30, left=60),
                                height=200,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "hello"
                                        )
                                    ]
                                )
                            )
                        ]

                    )
                ),
            ]
        )

    #  ------------------------// function for saving the records to the database here-//
    def save_contact_details_func(self):
        try:
            contact = ContactUs(
                self.first_name.value,
                self.last_name.value,
                self.email.value,
                self.phone_number.value,
                self.event_name.value,
                self.ordering_number.value,
                self.inquiry.value
            )
            contact.save_contact_details_func()
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
