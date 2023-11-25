import flet as ft
import json


class RegisterClass(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.email = ft.TextField(
            width=450,
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
            label="email".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.EMAIL,
            color="#311B92",
        )

        #  ------------------// control for the password here //----------------//
        self.password = ft.TextField(
            width=450,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.PASSWORD_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="password".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
            color="#311B92",
            can_reveal_password=True
        )

        self.register_modal = ft.AlertDialog(
            content=ft.Container(
                width=500,
                height=500,
                bgcolor="white",
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(top=30),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Image(
                                        src="assets/stickers/user-profile.png",
                                        height=150,
                                        width=150,
                                    )
                                ]
                            )
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.email
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.password
                            ]
                        ),

                        ft.Container(
                            margin=ft.margin.only(top=20),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.ElevatedButton(
                                        width=200,
                                        height=50,
                                        on_click=self.validate_fields_func,
                                        autofocus=True,
                                        color="white",
                                        bgcolor="#212121",
                                        elevation=None,
                                        icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                        text="register account".capitalize(),
                                        tooltip="register".capitalize()
                                    ),
                                ]
                            )
                        )

                    ]
                )
            )
        )

    def trigger_register_modal_func(self, e):
        try:
            self.page.dialog = self.register_modal
            self.register_modal.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    def validate_fields_func(self, e):
        try:
            if not self.email.value:
                self.email.error_text = "enter your email first".capitalize()
                self.page.update()
            #  ---------------// --------------------------//
            elif not self.password.value:
                self.password.error_text = "enter password".capitalize()
                self.page.update()
            else:
                self.register_clients()
        except Exception as ex:
            print(ex)

    #  --------------------// function to register new clients to the system---------//
    def register_clients(self):
        """the function will register new clients to the system"""
        try:
            with open('users.json', 'r') as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    # Handle the case where the file is empty or not valid JSON
                    users = {}
        except FileNotFoundError:
            users = {}

        if self.email in users:
            print("Username already exists. Please choose a different username.")
        else:
            users[self.email.value] = {'password': self.password.value}
            with open('users.json', 'w') as file:
                json.dump(users, file)
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "account created successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.page.dialog = self.register_modal
            self.register_modal.open = False
            self.page.update()

    def build(self):
        return ft.ListView()


class LoginCredentials(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.email = ft.TextField(
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
            label="email".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.EMAIL,
            color="#311B92",
        )

        #  ------------------// control for the password here //----------------//
        self.password = ft.TextField(
            width=480,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.PASSWORD_ROUNDED,
            prefix_style=ft.TextStyle(
                color="#311B92",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="#311B92"
            ),
            border_color="#0D47A1",
            label="password".capitalize(),
            label_style=ft.TextStyle(
                color="#311B92"
            ),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#0078D9",
            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
            color="#311B92",
            can_reveal_password=True
        )

    def validate_fields_func(self, e):
        try:
            if not self.email.value:
                self.email.error_text = "enter your email first".capitalize()
                self.page.update()
            #  ---------------// --------------------------//
            elif not self.password.value:
                self.password.error_text = "enter password".capitalize()
                self.page.update()
            else:
                self.login_credentials_func()
        except Exception as ex:
            print(ex)

    def login_credentials_func(self):
        try:
            with open('users.json', 'r') as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    # Handle the case where the file is empty or not valid JSON
                    users = {}
        except FileNotFoundError:
            print("No registered users. Please register first.")
            return

        if self.email.value in users and users[self.email.value]['password'] == self.password.value:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "logged in successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.page.go("/index")
            self.page.update()
        else:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#C21F1D",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "invalid username or password".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    def build(self):
        return ft.ListView(

        )


#   ----------------// the control //-------------------------//
class LoginControl(ft.UserControl):
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

        self.login_credentials = LoginCredentials(page=page)

        #  ----------------// register form //---------------//
        self.register_credentials = RegisterClass(page=page)

    #  --------------//-----------------//
    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[

                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "login or create account here".capitalize(),
                                color="#0050C1",
                                font_family="Raleway",
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    )
                ),
                #  ------------// the container for the register page-------//
                ft.Container(
                    width=800,
                    height=500,
                    margin=ft.margin.only(left=100, right=100, top=30),
                    border_radius=ft.border_radius.all(10),
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        blur_style=ft.ShadowBlurStyle.OUTER,
                        color="#311B92",

                    ),
                    content=ft.Column(
                        controls=[
                            #  -----------// container for the login form
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src="assets/streams/man (1).png",
                                            height=150,
                                            width=150
                                        )
                                    ]
                                )
                            ),

                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Column(
                                    controls=[

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                self.login_credentials.email
                                            ]
                                        ),

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                self.login_credentials.password
                                            ]
                                        ),

                                        ft.Container(
                                            margin=ft.margin.only(bottom=40),
                                            # margin=ft.margin.only(left=300),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=200,
                                                        height=50,
                                                        on_click=self.login_credentials.validate_fields_func,
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#311B92",
                                                        elevation=None,
                                                        icon=ft.icons.LOGIN_ROUNDED,
                                                        text="login".capitalize(),
                                                        tooltip="login".capitalize()
                                                    ),

                                                    ft.Divider(
                                                        height=30
                                                    ),
                                                    ft.ElevatedButton(
                                                        width=200,
                                                        height=50,
                                                        on_click=self.register_credentials.trigger_register_modal_func,
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#212121",
                                                        elevation=None,
                                                        icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                                        text="register account".capitalize(),
                                                        tooltip="register".capitalize()
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
            ]
        )
