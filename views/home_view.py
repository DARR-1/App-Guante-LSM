from typing import Union
import flet as ft
from Router import Router

def get_home_view(router: Union[Router, str, None] = None):
    body = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        margin=20,
        controls=[
            ft.Row(
                controls=[
                    ft.SearchBar(bar_hint_text="Search...", expand=True, aspect_ratio=7),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.BLACK,
                        expand=True,
                        padding=20,
                        aspect_ratio=0.5,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            ),
        ],
    )

    return body