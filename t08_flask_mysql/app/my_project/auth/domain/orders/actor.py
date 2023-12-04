"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Actors(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(45))
    salary = db.Column(db.Integer)
    name = db.Column(db.String(45))
    films_association = db.relationship("Actors_has_film", backref="actor")



    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Actors({self.id}, '{self.age}', '{self.sex}', '{self.salary}', '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        actor_films = [actors_film.put_into_dto() for actors_film in self.films_association]
        return {
            "id": self.id,
            "age": self.age,
            "sex": self.sex,
            "salary": self.salary,
            "name": self.name,
            "actor_films": actor_films,
            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actors:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Actors(
            age=dto_dict.get("age"),
            sex=dto_dict.get("sex"),
            salary=dto_dict.get("salary"),
            name=dto_dict.get("name"),

        )
        return obj
