"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Viewer


class ViewerDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Viewer

    def InsertRandomTables(self ):
        self._session.execute(text(
            f"CALL Cursor1();CALL InsertRandomTables()",))
        self._session.commit()
        return "Success"
