from Router import Router, DataStrategyEnum
from views.bienvenido_view import get_bview
from views.felicidades_view import get_fview 
from views.home_view import get_home_view

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    "/bienvenido": get_bview,
    "/felicidades": get_fview,
    "/home": get_home_view
}