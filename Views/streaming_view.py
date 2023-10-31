import flet as ft


def StreamingView(page):
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
    content = ft.ListView(
        expand=1,
        auto_scroll=True,
        spacing=10,
        height=800,
        scale=1.0,
        controls=[
            #  -------------------/the main container here/-------------------------------//
            ft.Container(
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(top=20, left=20),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "your streams".capitalize(),
                                                    color="#0050C1",
                                                    style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                    font_family="Raleway-bold",
                                                )
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        margin=ft.margin.only(right=20),
                                        content=ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    width=200,
                                                    height=50,
                                                    text="upload",
                                                    icon=ft.icons.UPLOAD_ROUNDED,
                                                    on_click={},
                                                    elevation=None,
                                                    bgcolor="#0078D9",
                                                    color="white"
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=10, right=10),
                            border_radius=ft.border_radius.all(10),
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#311B92",
                                    "black",
                                ],
                                begin=ft.alignment.bottom_left,
                                end=ft.alignment.top_right
                            ),
                            content=ft.Row(
                                #  ----------------the stack with the image here-----------//
                                controls=[
                                    #  ------------the container for the image here-------//
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Image(
                                                    height=400,
                                                    src=f"assets/streams/pexels-garrett-morrow-1649771.jpg",
                                                ),
                                            ]
                                        )
                                    ),
                                    #  ----------------the other container for the platforms------------------//
                                    ft.Container(
                                        margin=ft.margin.only(left=30),
                                        height=400,
                                        content=ft.Row(
                                            controls=[
                                                ft.Container(
                                                    width=300,
                                                    height=300,
                                                    bgcolor="white",
                                                    border_radius=ft.border_radius.all(10),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                margin=ft.margin.only(top=90),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.MISSED_VIDEO_CALL_ROUNDED,
                                                                            color="red",
                                                                            size=100
                                                                        )
                                                                    ]
                                                                ),
                                                                url="www.facebook.com"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                ft.Container(
                                                    width=300,
                                                    height=300,
                                                    bgcolor="white",
                                                    border_radius=ft.border_radius.all(10)
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )

        ]
    )
    return content
