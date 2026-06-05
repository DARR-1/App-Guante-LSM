from Router import Router, DataStrategyEnum
from views.bienvenido_view import get_bienvenido_view
from views.felicidades_view import get_felicidades_view 
from views.home_view import get_home_view
from views.modulos_view import get_modulos_view

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    "/bienvenido": get_bview,
    "/felicidades": get_fview,
    "/home": get_home_view,
    "/modulos": get_modulos_view,
}