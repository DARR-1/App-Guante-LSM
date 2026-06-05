from typing import Union
import flet as ft
from Router import Router

<<<<<<< HEAD
def get_bienvenido_view(router: Union[Router, str, None] = None):
=======
def get_bview(router: Union[Router, str, None] = None, page: ft.Page = None):
>>>>>>> 800edb5dfc990888f52fa1411609db90ddbad8ca

    body = ft.Container(
            expand=True, 
            image=ft.DecorationImage(
                src=f"/Bienvenido.gif", 
                fit=ft.BoxFit.COVER,
                ),
        )

    return body