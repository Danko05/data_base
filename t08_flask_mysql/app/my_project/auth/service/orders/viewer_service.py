"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import viewer_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ViewerService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = viewer_dao


    def InsertRandomTables(self ):
        result = self._dao.InsertRandomTables()
        return result

