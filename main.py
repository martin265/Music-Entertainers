import flet as ft
from Views.index_view import IndexView
from Routers.routes import Routers
from Controls.footer import MainFooter


# --------------------the main starting area for the application-------------//
def main(page: ft.Page):
    page.theme_mode = "light"
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
            else:
                print("it is black")
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
                                on_click=lambda _: page.go('/index'),
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
    ft.app(target=main, port=9090, view=ft.WEB_BROWSER, assets_dir="assets")
