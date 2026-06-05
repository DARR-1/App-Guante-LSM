from typing import Union
import flet as ft
from Router import Router

def get_home_view(router: Union[Router, str, None] = None):
    body = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        margin=ft.Margin(
            left=20,
            right=20,
            bottom=20,
            top=40,   # diferente
        ),
        spacing=20,
        controls=[
            ft.Row(
                controls=[
                    ft.SearchBar(
                        bar_hint_text="Search...",
                        expand=True,
                        aspect_ratio=8,
                        bar_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        bar_shape=ft.RoundedRectangleBorder(radius=10),
                        bar_leading=ft.Icon(ft.Icons.SEARCH, color=ft.Colors.BLACK),
                        bar_text_style=ft.TextStyle(
                            color=ft.Colors.WHITE,
                            size=14,
                        ),
                        bar_hint_text_style=ft.TextStyle(
                            color=ft.Colors.BLACK,
                            size=14,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Mundo Guante", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", size=10),
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text("Modos", size=20, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(src="/modo.jpg", fit=ft.BoxFit.CONTAIN),
                        bgcolor=ft.Colors.WHITE,
                        expand=True,
                        padding=20,
                        aspect_ratio=1,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Modo Traductor Clicked"),
                    ),
                    ft.Container(expand=True),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text("Lengua de Señas", size=20, weight=ft.FontWeight.BOLD),
        ],
    )

    return body