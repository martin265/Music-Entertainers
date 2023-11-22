import flet as ft


class MainFooter(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[

                        ]
                    )
                )
            ]
        )
