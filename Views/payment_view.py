import flet as ft


def PaymentView(page):
    content = ft.ListView(
        controls=[
            #  ---------// the main container here--------//
            ft.Container(
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