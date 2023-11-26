"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Actors_has_film(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "actors_has_film"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actors_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))





    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Actors_has_film({self.id},'{self.actors_id}', '{self.film_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "actors_id": self.actors_id,
            "film_id": self.film_id,


            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actors_has_film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Actors_has_film(
            id=dto_dict.get("id"),
            actors_id=dto_dict.get("actors_id"),
            film_id=dto_dict.get("film_id"),

        )
        return obj
