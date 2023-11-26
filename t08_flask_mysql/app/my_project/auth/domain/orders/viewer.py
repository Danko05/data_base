"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Viewer(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "viewer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    age = db.Column(db.String(45))
    reviews = db.relationship("Review", backref='film')




    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Viewer({self.id}, '{self.name}', '{self.age}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        review_list = [reviews.put_into_dto() for reviews in self.reviews]
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "review_list": review_list,

            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Viewer:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Viewer(
            name=dto_dict.get("name"),
            age=dto_dict.get("age"),
            review_list=dto_dict.get("review_list"),
        )
        return obj
