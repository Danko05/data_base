"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import viewer_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ViewerController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = viewer_service

    def InsertRandomTables(self):
        result = self._service.InsertRandomTables()
        return result
