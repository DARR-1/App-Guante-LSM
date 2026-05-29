import flet as ft

def NavBar(page):
    navbar = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    ft.Icons.HOME,
                    on_click=lambda e: page.go('/home')
                ),
                ft.IconButton(
                    ft.Icons.PERSON,
                    on_click=lambda e: page.go('/perfil')
                ),
                ft.Container(expand=True),
                ft.Text("By: Ya llegó Don Cangrejo", size=12, weight=ft.FontWeight.BOLD),
            ],
        )
    )

    return navbar