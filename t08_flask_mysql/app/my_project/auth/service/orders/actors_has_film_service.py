"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import actors_has_film_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class Actors_has_filmService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = actors_has_film_dao
    def insert_into_actor_film(self, actors_name, film_name):
        result = self._dao.insert_into_actor_film(actors_name,film_name)
        return result