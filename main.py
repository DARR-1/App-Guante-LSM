import asyncio
import flet as ft
from routes import router
from user_controls.app_bar import NavBar

#Constants:
#Delay_page:
DELAY_BIENVENIDO = 7
DELAY_FELICIDADES = 4
#Variables: 
#Delay_page:
delay_page = 0; 

async def delay_page(page: ft.Page, delay: int, route: str):
    await asyncio.sleep(delay)
    page.go(route)

def main(page: ft.Page):
    router.page = page

    page.fonts = {
        "Quicksand": "/Quicksand-Bold.ttf",
        "Krabby Patty": "/Krabby Patty.ttf"
    }
    page.padding = 0
    page.update()

    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    
    page.go('/bienvenido')

    page.bottom_appbar = NavBar(page)

    asyncio.create_task(delay_page(page, DELAY_BIENVENIDO, '/home'))

ft.run(
    main,
    assets_dir="assets",
)