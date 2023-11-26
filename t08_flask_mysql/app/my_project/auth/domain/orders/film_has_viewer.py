"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Film_has_viewer(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "film_has_viewer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    viewer_id = db.Column(db.Integer, db.ForeignKey('viewer.id'))





    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Facts({self.id},'{self.film_id}', '{self.viewer_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "film_id": self.film_id,
            "viewer_id": self.viewer_id,


            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Film_has_viewer:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Film_has_viewer(
            id=dto_dict.get("id"),
            film_id=dto_dict.get("film_id"),
            viewer_id=dto_dict.get("viewer_id"),

        )
        return obj
