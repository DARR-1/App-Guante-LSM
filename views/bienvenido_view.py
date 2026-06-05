from typing import Union
import flet as ft
from Router import Router

def get_bienvenido_view(router: Union[Router, str, None] = None):

    body = ft.Container(
            expand=True, 
            image=ft.DecorationImage(
                src=f"/Bienvenido.gif", 
                fit=ft.BoxFit.COVER,
                ),
        )

    return body