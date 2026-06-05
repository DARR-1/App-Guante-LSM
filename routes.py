from Router import Router, DataStrategyEnum
from views.bienvenido_view import get_bienvenido_view
from views.felicidades_view import get_felicidades_view 
from views.home_view import get_home_view

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    "/bienvenido": get_bienvenido_view,
    "/felicidades": get_felicidades_view,
    "/home": get_home_view
}