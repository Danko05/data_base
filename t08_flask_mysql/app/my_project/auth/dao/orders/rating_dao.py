"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Rating


class RatingDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Rating

    def CallGetMaxRating(self):
        result = self._session.execute(text(
            f"Call GetMaxRating()",))
        return result.scalar()
