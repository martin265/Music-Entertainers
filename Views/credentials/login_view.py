import flet as ft
import json


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
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[

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
                                            # margin=ft.margin.only(left=300),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        width=200,
                                                        height=50,
                                                        on_click={},
                                                        autofocus=True,
                                                        color="white",
                                                        bgcolor="#311B92",
                                                        elevation=None,
                                                        icon=ft.icons.LOGIN_ROUNDED,
                                                        text="login".capitalize(),
                                                        tooltip="login".capitalize()
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
            ]
        )
