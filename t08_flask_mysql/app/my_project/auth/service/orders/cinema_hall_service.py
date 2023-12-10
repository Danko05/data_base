"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import cinema_hall_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class Cinema_hallService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = cinema_hall_dao
