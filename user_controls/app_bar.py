import flet as ft


def NavBar(page):



    NavBar = ft.AppBar(
            leading=ft.Icon(ft.Icons.TAG_FACES_ROUNDED),
            leading_width=40,
            title=ft.Text("Flet Router"),
            center_title=False,
            bgcolor=ft.Colors.DEEP_PURPLE,
            actions=[
                ft.IconButton(ft.Icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.Icons.PERSON_ROUNDED, on_click=lambda _: page.go('/profile')),
                ft.IconButton(ft.Icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings'))
            ]
        )

    return NavBar
