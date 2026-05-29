import flet as ft


import flet as ft

def NavBar(page):
    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        expand=True,
        on_change=lambda e: page.go(['/home', '/perfil'][e.control.selected_index])
    )

    navbar = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                nav,
                ft.Text("By: Ya llegó Don Cangrejo", size=12, weight=ft.FontWeight.BOLD),
            ],
        )
    )

    return navbar