"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Film


class FilmDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Film

    def insert_rows(self):
        self._session.execute(text("CALL InsertRows()"))
        self._session.commit()
        return "Success"
