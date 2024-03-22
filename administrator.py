import flet as ft
from Administrator.pages.dashboard import MainDashboard
from Administrator.pages.events import EventsPage
from Administrator.pages.payments import Payments
from Administrator.pages.report import FinancialReports


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    #  -----------------// functions for the page transitions here---------//
    all_pages = [
        MainDashboard(page=page),
        EventsPage(page=page),
        Payments(page=page),
        FinancialReports(page=page)
    ]

    #  --------------function for transitioning the pages------------------//
    def transition_through_pages():
        try:
            for index, single_page in enumerate(all_pages):
                single_page.visible = True if index == navigation_rail.selected_index else False
                page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()

    #  ---------------------------the function to find the selected page here----------//
    def destination_page(e):
        try:
            transition_through_pages()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()

    #  ---------------the navigation for the administrator---------------//
    navigation_rail = ft.NavigationRail(
        leading=ft.FloatingActionButton(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Image(
                            src="assets/icons/wave-sound.png",
                            height=50,
                            width=50
                        )
                    ]
                )
            )
        ),
        selected_index=0,
        group_alignment=-0.9,
        min_width=80,
        min_extended_width=150,
        extended=False,
        #  -----------------the destinations here for the navigation-----------//
        destinations=[
            #  ------------------------//may the good Lord Jesus Christ be with us all---------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.SPACE_DASHBOARD,
                    tooltip="dashboard".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "home".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  ------------// the destination for the events page here-----//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.EVENT_NOTE_ROUNDED,
                    tooltip="events".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "events".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  ------------// the destination for the events page here-----//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.PAYMENT_ROUNDED,
                    tooltip="payments".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "payment".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),

            #  ------------// the destination for the events page here-----//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.REPORT_ROUNDED,
                    tooltip="reports".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "report".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            )


        ],
        on_change=destination_page
    )
    transition_through_pages()

    #  -----------------------adding the page controls to the main window here---------//
    page.add(
        ft.Row(
            controls=[
                navigation_rail,
                ft.Column(all_pages, alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", port=9090)
