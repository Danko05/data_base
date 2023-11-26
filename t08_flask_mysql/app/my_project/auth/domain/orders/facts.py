"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Facts(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "facts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer)
    time = db.Column(db.Float)
    genre = db.Column(db.String(45))
    award = db.Column(db.Integer)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))





    def __repr__(self) -> str:
        return f"Facts({self.id}, '{self.price}', '{self.time}', '{self.genre}', '{self.award}', '{self.film_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "price": self.price,
            "time": self.time,
            "genre": self.genre,
            "award": self.award,
            "film_id": self.film_id,
            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Facts:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Facts(
            price=dto_dict.get("price"),
            time=dto_dict.get("time"),
            genre=dto_dict.get("genre"),
            award=dto_dict.get("award"),
            film_id=dto_dict.get("film_id"),
        )
        return obj
