import flet as ft
from Views.index_view import IndexView
from Routers.routes import Routers
from Controls.footer import MainFooter
import json
from flet_multi_page import subPage


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
            p = subPage(target=main)
            p.start()
            self.page.window_close()
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


def login_page(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.theme_mode = "light"
    page.window_center()
    page.fonts = {
        "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
        "Raleway": "assets/fonts/static/Raleway-Light.ttf",
        "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
        "Roboto-black": "assets/fonts/Roboto-Black.ttf",
        "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
    }

    login_credentials = LoginCredentials(page=page)

    #  ----------------// register form //---------------//
    register_credentials = RegisterClass(page=page)

    page.add(
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
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[

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
                                                login_credentials.email
                                            ]
                                        ),

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                login_credentials.password
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
                                                        on_click=login_credentials.validate_fields_func,
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
                                                        on_click=register_credentials.trigger_register_modal_func,
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
    )


# --------------------the main starting area for the application-------------//
def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_center()
    page.update()
    #  ----------------//removing the default padding and margins----------------//
    page.space = 0
    page.padding = 0
    page.update()
    #  --------------------updating the controls here----------------//
    #  --------------// using custom fonts here---------------//
    page.fonts = {
        "Raleway": "assets/fonts/static/OpenSans-Light.ttf"
    }
    page.theme = ft.Theme(font_family="Raleway")
    page.update()

    #  --------------------page routers here--------------//
    myRouter = Routers(page)
    #  -----------------on route change here----------//
    page.on_route_change = myRouter.route_change

    #  -------------------------//--------------------------//
    def on_hover(e):
        e.control.color = "blue" if e.data == "true" else "red"
        e.control.update()

    #  ---------// all the controls for the pop menu will be here-----------//
    def check_item_clicked(e):
        """the function will be triggered when the menu button is clicked here"""
        try:
            e.control.checked = not e.control.checked
            if not e.control.checked == "light":
                print("true it is light")
            elif e.control.checked == "dark":
                print("dark theme activated")
        except Exception as ex:
            print(ex)

    #  -----------------// Navigation //-----------------//
    navigation_bar = ft.Container(
        padding=ft.padding.all(0),
        gradient=ft.LinearGradient(
            colors=[
                "#0078D9",
                "#311B92",
            ],
            begin=ft.alignment.top_right,
            end=ft.alignment.bottom_left
        ),
        height=80,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                #  ------------for the links---------//
                ft.Container(
                    margin=ft.margin.only(right=30),
                    content=ft.Row(
                        controls=[
                            #  -------------------the container for the logo here----------//
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                            src=f"assets/icons/wave-sound.png",
                                            height=50,
                                            width=50,
                                            color="white",
                                            semantics_label="logo"
                                        )
                                    ]
                                )
                            ),
                            #  ----------------------// the container for the links here-------//
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                ink=False,
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "home".title(),
                                            color="white",
                                            size=15
                                        )
                                    ]
                                ),
                                on_click=lambda _: page.go('/'),
                            ),
                            ft.Divider(),
                            #  -------------the other controls here-------//
                            #  -------------the other controls here-------//
                            ft.Container(
                                ink=False,
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "tickets".title(),
                                            color="white",
                                            size=15
                                        ),

                                    ]
                                ),
                                on_click=lambda _: page.go('/tickets'),
                            ),
                            ft.Divider(),
                            #  -------------the other controls here-------//
                            ft.Container(
                                ink=False,
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "events".title(),
                                            color="white",
                                            size=15,
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            weight=ft.FontWeight.W_100
                                        )
                                    ]
                                ),
                                on_click=lambda _: page.go('/events'),
                            ),
                            #  -------------the other controls here-------//
                            ft.Divider(),
                            #  -------------the other controls here-------//
                            ft.Container(
                                ink=False,
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "streams".title(),
                                            color="white",
                                            size=15,
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            weight=ft.FontWeight.W_100
                                        )
                                    ]
                                ),
                                on_click=lambda _: page.go('/streams'),
                                on_hover=on_hover
                            ),
                            ft.Divider(),
                            #  -------------the other controls here-------//
                            ft.Container(
                                ink=False,
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "contact".title(),
                                            color="white",
                                            size=15,
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            weight=ft.FontWeight.W_100
                                        )
                                    ]
                                ),
                                on_click=lambda _: page.go('/contact'),
                                on_hover=on_hover
                            ),
                        ]
                    )
                ),
                #  -------------------------the container that will hold the icons here---------//
                ft.Container(
                    width=20,
                    margin=ft.margin.only(right=40),
                    content=ft.Row(
                        controls=[
                            #  -------------// the icon button for the theme modes here------//
                            ft.PopupMenuButton(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.icons.COLOR_LENS_ROUNDED,
                                            color="white",
                                            size=30
                                        )
                                    ]
                                ),
                                items=[
                                    #   ----------// the items to be selected by the user here------//
                                    ft.PopupMenuItem(
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "select theme".capitalize()
                                                )
                                            ]
                                        )
                                    ),
                                    #   ----------// the items to be selected by the user here------//
                                    ft.PopupMenuItem(
                                        checked=False,
                                        on_click=check_item_clicked,
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "light".capitalize()
                                                )
                                            ]
                                        )
                                    ),
                                    #   ----------// the items to be selected by the user here------//
                                    ft.PopupMenuItem(
                                        checked=False,
                                        on_click=check_item_clicked,
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "dark".capitalize()
                                                )
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    )
                )
                #  ---------------------// container ends here---------------------//

            ]
        )

    )

    page.add(
        ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                navigation_bar,
                myRouter.body,
                MainFooter(page=page)
            ]
        )
    )
    page.go("/")
    page.update()


if __name__ == "__main__":
    ft.app(target=login_page, port=9090, assets_dir="assets")
