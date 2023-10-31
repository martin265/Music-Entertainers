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
    content = ft.Container(
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                #  -------------// the container for the streams page------------//
                ft.Container(
                    height=500,
                    margin=ft.margin.only(left=10, right=10),
                    border_radius=ft.border_radius.all(10),
                    gradient=ft.LinearGradient(
                        colors=[
                            "#311B92",
                            "#0078D9",
                        ],
                        begin=ft.alignment.bottom_left,
                        end=ft.alignment.top_right
                    ),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "your audio streams and uploads",
                                size=24,
                                font_family="Raleway-bold"
                            )
                        ]
                    )
                ),
                ft.Container(
                    height=500,
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
                        controls=[
                            ft.Text(
                                "your audio streams and uploads",
                                size=24,
                                font_family="Raleway-bold"
                            )
                        ]
                    )
                )
            ]
        )
    )
    return content