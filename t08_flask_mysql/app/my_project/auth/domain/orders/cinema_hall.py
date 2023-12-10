"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Cinema_hall(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "cinema_hall"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cinema_id = db.Column(db.Integer)


    def __repr__(self) -> str:
        return f"Cinema_hall({self.id}, '{self.cinema_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "cinema_id": self.cinema_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Cinema_hall:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Cinema_hall(
            cinema_id=dto_dict.get("cinema_id"),
        )
        return obj
