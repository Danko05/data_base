"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import rating_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class RatingController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = rating_service

    def CallGetMaxRating(self):
        result = self._service.CallGetMaxRating()
        return result
