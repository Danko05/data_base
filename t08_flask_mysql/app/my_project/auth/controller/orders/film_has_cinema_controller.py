"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import film_has_cinema_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class Film_has_cinemaController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = film_has_cinema_service
