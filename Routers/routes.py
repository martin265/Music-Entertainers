import flet as ft
from Views.index_view import IndexView
from Views.account_view import AccountView
from Views.payment_view import PaymentView
from Views.streaming_view import StreamingView
from Views.events_view import EventsView
from Views.contact_us_view import ContactView
from Views.credentials.login_view import LoginControl


class Routers:
    """class that will handle all the page transitions"""
    def __init__(self, page: ft.Page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/tickets": PaymentView(page),
            "/events": EventsView(page),
            "/streams": StreamingView(page),
            "/contact": ContactView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    # the route change function will be here---------------//
    def route_change(self, route):
        try:
            self.body.content = self.routes[route.route]
            self.body.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
