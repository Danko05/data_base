"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import rating_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class RatingService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = rating_dao

    def CallGetMaxRating(self):
        result = self._dao.CallGetMaxRating()
        return result
