import flet as ft
import requests
from bs4 import BeautifulSoup


class StreamingView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.fonts = {
            "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
            "Raleway": "assets/fonts/static/Raleway-Light.ttf",
            "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
            "Roboto-black": "assets/fonts/Roboto-Black.ttf",
            "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
        }
        self.favourite_chips = ft.Chip(
            label=ft.Text("Save to favourites"),
            leading=ft.Icon(ft.icons.FAVORITE_BORDER_OUTLINED),
            bgcolor="#0050C1",
            disabled_color="#0050C1",
            autofocus=True,
            on_click={},
            width=300,
        )

    #  ----------// the function will be triggered when the container is hovered

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            #  -----------// main container to wrap the controls here-----//
            controls=[
                ft.Container(
                    margin=ft.margin.only(left=30, top=30),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "streams".capitalize(),
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                color="#0050C1",
                                font_family="Raleway-bold"
                            )
                        ]
                    )
                ),
                #  -------------// container for the chips-------------//
                ft.Container(
                    content=ft.Column(
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            #  ----------------// the first row for the cards-----//
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        #  --------------// first container here-----//
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            width=350,
                                            height=430,
                                            ink=False,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#4A148C",
                                                    "#4A4453"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_right

                                            ),
                                            shadow=ft.BoxShadow(
                                                blur_radius=4,
                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                color="#311B92",
                                            ),
                                            #  ---------------// the content for the container----//
                                            content=ft.Column(
                                                controls=[
                                                    #  ------// container for the image-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src=f"assets/streams/pexels-jorge-fakhouri-filho-2701570.jpg",
                                                                    fit=ft.ImageFit.COVER,
                                                                    height=300,
                                                                    width=300,
                                                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                                                    border_radius=ft.border_radius.all(10),
                                                                    semantics_label="hello"
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    #  -------------// for the burron
                                                    ft.Container(
                                                        margin=ft.margin.only(top=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.IconButton(
                                                                    icon=ft.icons.API_ROUNDED,
                                                                    icon_size=60,
                                                                    icon_color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            animate=True,
                                            animate_size=800,
                                            on_click=lambda e: self.page.launch_url("https://www.youtube.com/"),
                                            tooltip="open youtube".capitalize()
                                        ),
                                        #  --------------------//2------------------------//
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            width=350,
                                            height=430,
                                            ink=False,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#4A148C",
                                                    "#A50084"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_right

                                            ),
                                            shadow=ft.BoxShadow(
                                                blur_radius=4,
                                                blur_style=ft.ShadowBlurStyle.INNER,
                                                color="#311B92",
                                            ),
                                            #  ---------------// the content for the container----//
                                            content=ft.Column(
                                                controls=[
                                                    #  ------// container for the image-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src=f"assets/streams/pexels-yente-van-eynde-2403054.jpg",
                                                                    fit=ft.ImageFit.COVER,
                                                                    height=300,
                                                                    width=300,
                                                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                                                    border_radius=ft.border_radius.all(10),
                                                                    semantics_label="hello"
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    #  -------------// for the burron
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, top=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.IconButton(
                                                                    icon=ft.icons.APPLE_ROUNDED,
                                                                    icon_size=60,
                                                                    icon_color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            animate=True,
                                            animate_size=800,
                                            on_click=lambda e: self.page.launch_url("https://tv.apple.com/"),
                                            tooltip="open youtube".capitalize()
                                        ),
                                        #  --------------------//3------------------------//
                                        ft.Container(
                                            margin=ft.margin.only(top=30),
                                            width=350,
                                            height=430,
                                            ink=False,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#4A148C",
                                                    "#E52E6A"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_right

                                            ),
                                            shadow=ft.BoxShadow(
                                                blur_radius=4,
                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                color="#311B92",
                                            ),
                                            #  ---------------// the content for the container----//
                                            content=ft.Column(
                                                controls=[
                                                    #  ------// container for the image-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src=f"assets/streams/pexels-antoni-shkraba-production-8044178.jpg",
                                                                    fit=ft.ImageFit.COVER,
                                                                    height=300,
                                                                    width=300,
                                                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                                                    border_radius=ft.border_radius.all(10),
                                                                    semantics_label="hello"
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    #  -------------// for the burron
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, top=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.IconButton(
                                                                    icon=ft.icons.MOVIE_FILTER_ROUNDED,
                                                                    icon_size=60,
                                                                    icon_color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            animate=True,
                                            animate_size=800,
                                            on_click=lambda e: self.page.launch_url("https://www.netflix.com/mw/"),
                                            tooltip="open youtube".capitalize()
                                        ),
                                    ]
                                )
                            ),
                            #  ---------------// the second row for the cards-------//
                            ft.Container(
                                bgcolor="#eceff1",
                                height=400,
                                margin=ft.margin.only(top=20),
                                content=ft.Column(
                                    controls=[
                                        #  ------------// container for the top text--------//
                                        ft.Container(
                                            margin=ft.margin.only(top=10),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "platforms".capitalize(),
                                                        style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                        color="#0050C1",
                                                        font_family="Raleway-bold"
                                                    )
                                                ]
                                            )
                                        ),
                                        #  -------// container for the supported platforms here-----//
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    #  -------// the first card container----------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30, left=20),
                                                        width=250,
                                                        height=150,
                                                        border_radius=ft.border_radius.all(10),
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                ft.colors.WHITE,
                                                                ft.colors.WHITE
                                                            ],
                                                            begin=ft.alignment.top_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        shadow=ft.BoxShadow(
                                                            blur_radius=9,
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                            color="#bf360c",
                                                        ),
                                                        content=ft.Column(
                                                            controls=[
                                                                #  ---------// container for the icon
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Container(
                                                                                margin=ft.margin.only(top=30),
                                                                                content=ft.Image(
                                                                                    src="assets/icons/youtube.png",
                                                                                    height=100,
                                                                                    width=100
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------// the first card container----------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30, left=20),
                                                        width=250,
                                                        height=150,
                                                        border_radius=ft.border_radius.all(10),
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                ft.colors.WHITE,
                                                                ft.colors.WHITE
                                                            ],
                                                            begin=ft.alignment.top_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        shadow=ft.BoxShadow(
                                                            blur_radius=9,
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                            color="#bf360c",
                                                        ),
                                                        content=ft.Column(
                                                            controls=[
                                                                #  ---------// container for the icon
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Container(
                                                                                margin=ft.margin.only(top=30),
                                                                                content=ft.Image(
                                                                                    src="assets/icons/netflix.png",
                                                                                    height=100,
                                                                                    width=100
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    # -------------------// card number 4---------------------//
                                                    #  -------// the first card container----------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30, left=20),
                                                        width=250,
                                                        height=150,
                                                        border_radius=ft.border_radius.all(10),
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                ft.colors.WHITE,
                                                                ft.colors.WHITE
                                                            ],
                                                            begin=ft.alignment.top_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        shadow=ft.BoxShadow(
                                                            blur_radius=9,
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                            color="#005C3B",
                                                        ),
                                                        content=ft.Column(
                                                            controls=[
                                                                #  ---------// container for the icon
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Container(
                                                                                margin=ft.margin.only(top=30),
                                                                                content=ft.Image(
                                                                                    src="assets/icons/spotify.png",
                                                                                    height=100,
                                                                                    width=100
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------// the first card container----------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30, left=20),
                                                        width=250,
                                                        height=150,
                                                        border_radius=ft.border_radius.all(10),
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                ft.colors.WHITE,
                                                                ft.colors.WHITE
                                                            ],
                                                            begin=ft.alignment.top_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        shadow=ft.BoxShadow(
                                                            blur_radius=9,
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                            color="#A56B58",
                                                        ),
                                                        content=ft.Column(
                                                            controls=[
                                                                #  ---------// container for the icon
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Container(
                                                                                margin=ft.margin.only(top=30),
                                                                                content=ft.Image(
                                                                                    src="assets/icons/deer.png",
                                                                                    height=100,
                                                                                    width=100
                                                                                )
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
                                        #  ------------------------// container for the footer here--------//

                                    ]
                                )
                            ),
                            #  ----------------------//-------------------//--------------//
                            ft.Container(
                                height=400,
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#4A148C",
                                        "#4A4453"
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right

                                ),
                                content=ft.Row(
                                    controls=[

                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]
        )
