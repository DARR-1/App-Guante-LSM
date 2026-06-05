from typing import Union
import flet as ft
from Router import Router

def get_modulos_view(router: Union[Router, str, None] = None, page: ft.Page = None):
    body = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        margin=ft.Margin(
            left=20,
            right=20,
            bottom=0,
            top=0,
        ),
        spacing=20,
        scroll=ft.ScrollMode.HIDDEN,
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Módulos", size=24, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                margin=ft.Margin(top=40)
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    image=ft.DecorationImage(
                                        src="MedusaRosa.jpg",
                                        fit=ft.BoxFit.COVER,
                                    ),
                                    shape=ft.BoxShape.CIRCLE,
                                    expand=True
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Módulo 1", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Descripción del módulo 1.", size=10),
                                    ],
                                    expand=True,
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Módulo 1 clickeado"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    image=ft.DecorationImage(
                                        src="MedusaAzul.jpg",
                                        fit=ft.BoxFit.COVER,
                                    ),
                                    shape=ft.BoxShape.CIRCLE,
                                    expand=True
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Módulo 2", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Descripción del módulo 2.", size=10),
                                    ],
                                    expand=True,
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Módulo 2 clickeado"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    image=ft.DecorationImage(
                                        src="MedusaMorada.jpg",
                                        fit=ft.BoxFit.COVER,
                                    ),
                                    shape=ft.BoxShape.CIRCLE,
                                    expand=True
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Módulo 3", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Descripción del módulo 3.", size=10),
                                    ],
                                    expand=True,
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Módulo 3 clickeado"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    image=ft.DecorationImage(
                                        src="MedusaVerde.jpg",
                                        fit=ft.BoxFit.COVER,
                                    ),
                                    shape=ft.BoxShape.CIRCLE,
                                    expand=True
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Módulo 4", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Descripción del módulo 4.", size=10),
                                    ],
                                    expand=True,
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Módulo 4 clickeado"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    image=ft.DecorationImage(
                                        src="MedusaAmarilla.jpg",
                                        fit=ft.BoxFit.COVER,
                                    ),
                                    shape=ft.BoxShape.CIRCLE,
                                    expand=True
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Módulo 5", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Descripción del módulo 5.", size=10),
                                    ],
                                    expand=True,
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Módulo 5 clickeado"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    image=ft.DecorationImage(
                                        src="MedusaNaranja.jpg",
                                        fit=ft.BoxFit.COVER,
                                    ),
                                    shape=ft.BoxShape.CIRCLE,
                                    expand=True
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Módulo 6", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Descripción del módulo 6.", size=10),
                                    ],
                                    expand=True,
                                )
                            ]
                        ),
                        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                        expand=True,
                        padding=20,
                        aspect_ratio=2,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _: print("Módulo 6 clickeado"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        ],
    )

    return body