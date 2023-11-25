import flet as ft
import time, threading


class IndexView(ft.UserControl):
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

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  //----------------the top container here//-------------------//
                ft.Container(
                    margin=ft.margin.only(top=30),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "welcome to malawi music entertainers".capitalize(),
                                color="#212121",
                                font_family="Raleway",
                                style=ft.TextThemeStyle.DISPLAY_SMALL
                            )
                        ]
                    )
                ),

                ft.Container(
                    content=ft.Row(
                        controls=[

                        ]
                    )
                ),

                #  --------------// container for the key features here // ------------------//

                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "key features".capitalize(),
                                            color="#212121",
                                            font_family="Raleway",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                )
                            ),

                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Container(
                                            height=500,
                                            width=400,
                                            bgcolor="black",
                                        ),

                                        ft.Container(
                                            height=500,
                                            width=400,
                                            bgcolor="black",
                                        ),

                                        ft.Container(
                                            height=500,
                                            width=400,
                                            bgcolor="black",
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                ),

                ft.Container(
                    height=600,
                    margin=ft.margin.only(top=30),
                    shadow=ft.BoxShadow(
                        blur_radius=20,
                        blur_style=ft.ShadowBlurStyle.OUTER,
                        color="#311B92",
                    ),
                    content=ft.Image(
                        height=600,
                        src="assets/images/cards/pexels-mikky-k-625644.jpg",
                        fit=ft.ImageFit.CONTAIN,
                        repeat=ft.ImageRepeat.REPEAT
                    )
                ),

                ft.Container(
                    margin=ft.margin.only(top=30),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "trending artists".capitalize(),
                                color="#212121",
                                font_family="Raleway",
                                style=ft.TextThemeStyle.DISPLAY_SMALL
                            )
                        ]
                    )
                ),

                #  //---------------------// footer //-----------------------//
                ft.Container(
                    height=230,
                    margin=ft.margin.only(top=20, bottom=40),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                height=200,
                                width=200,
                                shadow=ft.BoxShadow(
                                    blur_radius=10,
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                    color="#0075D9",
                                ),
                                shape=ft.BoxShape.CIRCLE,
                                bgcolor="black",
                                content=ft.Image(
                                    src="assets/images/cards/pexels-wendy-wei-1387174.jpg",
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.REPEAT,
                                    border_radius=ft.border_radius.all(300)
                                )
                            ),

                            #  ------------------// ---------------------//
                            ft.Container(
                                height=200,
                                width=200,
                                shadow=ft.BoxShadow(
                                    blur_radius=10,
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                    color="#0075D9",
                                ),
                                shape=ft.BoxShape.CIRCLE,
                                bgcolor="black",
                                content=ft.Image(
                                    src="assets/images/cards/pexels-wendy-wei-1387174.jpg",
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.REPEAT,
                                    border_radius=ft.border_radius.all(300)
                                )
                            ),

                            #  --------------------// ------------------//
                            ft.Container(
                                height=200,
                                width=200,
                                shadow=ft.BoxShadow(
                                    blur_radius=10,
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                    color="#0075D9",
                                ),
                                shape=ft.BoxShape.CIRCLE,
                                bgcolor="black",
                                content=ft.Image(
                                    src="assets/images/cards/pexels-wendy-wei-1387174.jpg",
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.REPEAT,
                                    border_radius=ft.border_radius.all(300)
                                )
                            ),

                            #  -----------------// -------------------//
                            ft.Container(
                                height=200,
                                width=200,
                                shadow=ft.BoxShadow(
                                    blur_radius=10,
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                    color="#0075D9",
                                ),
                                shape=ft.BoxShape.CIRCLE,
                                bgcolor="black",
                                content=ft.Image(
                                    src="assets/images/cards/pexels-wendy-wei-1387174.jpg",
                                    fit=ft.ImageFit.FILL,
                                    border_radius=ft.border_radius.all(300)
                                )
                            ),

                        ]
                    )
                ),

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
