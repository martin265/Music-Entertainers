import flet as ft


def MainFooter(page):
    content = ft.ListView(
        controls=[
            # -------------------// the main container for the footer here--------//
            ft.Container(
                height=600,
                margin=0,
                padding=0,
                bgcolor="black",
                content=ft.Column(
                    controls=[

                    ]
                )
            )
        ]
    )
    return content
