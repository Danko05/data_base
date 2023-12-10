"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Box_office_fees


class Box_office_feesDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Box_office_fees

    # def find_by_name(self, name: str) -> List[object]:
    #     """
    #     Gets Client objects from database table by field name.
    #     :param name: name value
    #     :return: search objects
    #     """
    #     return self._session.query(Box_office_fees).filter(Box_office_fees.name == name).order_by(Box_office_fees.name).all()
    #
    # def find_by_number(self, number: int) -> List[object]:
    #     """
    #     Gets Client objects from database table by field 'number'.
    #     :param number: number value
    #     :return: search objects
    #     """
    #     return self._session.query(Box_office_fees).filter(Box_office_fees.number == number).order_by(Box_office_fees.number.desc()).all()

    def insert_box_office_fees(self, revenu):
        self._session.execute(text(
            f"CALL insert_box_office_fees({revenu})",
        ))
        self._session.commit()
        return "Success"
