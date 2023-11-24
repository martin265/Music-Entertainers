import flet as ft


def AccountView(page):
    content = ft.ListView(
        controls=[
            #  ---------// the main container here--------//
            ft.Container(
                width=1000,
                height=750,
                margin=ft.margin.only(left=100, right=100, top=30),
                border_radius=ft.border_radius.all(10),
                shadow=ft.BoxShadow(
                    blur_radius=10,
                    blur_style=ft.ShadowBlurStyle.OUTER,
                    color="#311B92",

                ),
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "hello"
                        )
                    ]
                )
            )
        ]
    )
    return content