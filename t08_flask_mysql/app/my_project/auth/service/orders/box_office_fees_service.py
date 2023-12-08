"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import box_office_fees_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class Box_office_feesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = box_office_fees_dao

    def insert_box_office_fees(self, revenu):
        result = self._dao.insert_box_office_fees(revenu)
        return result
