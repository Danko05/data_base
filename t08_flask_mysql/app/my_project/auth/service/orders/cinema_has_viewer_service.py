"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import cinema_has_viewer_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class Cinema_has_viewerService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = cinema_has_viewer_dao
