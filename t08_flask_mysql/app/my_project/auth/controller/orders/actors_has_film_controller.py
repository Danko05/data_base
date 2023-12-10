"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import actors_has_film_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class Actors_has_filmController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = actors_has_film_service

    def insert_into_actor_film(self, actors_name, film_name):
        result = self._service.insert_into_actor_film(actors_name,film_name)
        return result
