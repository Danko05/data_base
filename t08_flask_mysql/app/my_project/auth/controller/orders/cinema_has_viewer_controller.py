"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import cinema_has_viewer_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class Cinema_has_viewerController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = cinema_has_viewer_service
