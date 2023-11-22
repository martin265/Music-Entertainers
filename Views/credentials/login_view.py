import flet as ft
import json


#   ----------------// the control //-------------------------//
class LoginControl(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    #  --------------//-----------------//
    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  ------------// the container for the register page-------//
                ft.Container(
                    content=ft.Row(
                        controls=[

                        ]
                    )
                )
            ]
        )
