import flet as ft


def AccountView(page):
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