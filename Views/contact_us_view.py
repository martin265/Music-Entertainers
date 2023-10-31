import flet as ft
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def ContactView(page):
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
    #  ----------------// the input fields for the collection here-------------//
    first_name = ft.TextField(
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
    last_name = ft.TextField(
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
    email = ft.TextField(
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
    phone_number = ft.TextField(
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
    event_name = ft.TextField(
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
    ordering_number = ft.TextField(
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
    inquiry = ft.TextField(
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
    def validate_contact_inputs(e):
        """the function to validate the user inputs"""
        try:
            if not first_name.value:
                first_name.error_text = "fill in the blanks".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            #  -------------------//----------------------------//
            elif not last_name.value:
                last_name.error_text = "enter your last name".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            #  -----------------------//------------------------//
            elif not email.value:
                email.error_text = "fill in the email address".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            #  --------------------------//--------------------------//
            elif not phone_number.value:
                phone_number.error_text = "enter your phone number".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            #  --------------------------------//--------------------//
            elif not event_name.value:
                event_name.error_text = "add an event first".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            #  -------------------------//-------------------------//
            elif not ordering_number.value:
                ordering_number.error_text = "enter the ordering number".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            #  ------------------------//----------------------------//
            elif not inquiry.value:
                inquiry.error_text = "type in some inquiry message".capitalize()
                page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "fill in the blanks first".capitalize()
                            )
                        ]
                    )
                )
                page.snack_bar.open = True
                page.update()
            else:
                send_email_notification()
        except Exception as e:
            print(e)

    #  --------------------// the function will send the email address to the clients-------//
    def send_email_notification():
        try:
            #  ---------------------// the codes for sending the email notifications here-----------//
            # Gmail account details
            sender_email = "martinsilungwe12@gmail.com"
            sender_password = "Pa55word@900!"

            # Gmail SMTP server
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Email content
            subject = "Subject of the Email"
            recipient_email = email.value
            email_body = inquiry.value

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
            print("Email sent successfully")

        except Exception as e:
            print(e)

    #  ------------------//--------------------------------//
    content = ft.ListView(
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
                                                ft.Row([first_name, last_name]),
                                                ft.Row([email, phone_number]),
                                                ft.Row([event_name, ordering_number]),
                                                ft.Row([inquiry]),
                                                #  --------------//-------------//
                                                ft.Container(
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.ElevatedButton(
                                                                width=200,
                                                                height=50,
                                                                text="contact us".capitalize(),
                                                                icon=ft.icons.PERM_CONTACT_CALENDAR_ROUNDED,
                                                                on_click=validate_contact_inputs,
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
    return content
