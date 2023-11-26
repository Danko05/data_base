"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Film(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    ratings = db.relationship("Rating", backref='film')
    fact = db.relationship("Facts", backref='film')
    box_office_fees = db.relationship("Box_office_fees", backref='film')
    reviews = db.relationship("Review", backref='film_r')
    actors_association = db.relationship("Actors_has_film", backref="film")






    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Facts({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        rating_list = [rating.put_into_dto() for rating in self.ratings]
        fact_list = [fact.put_into_dto() for fact in self.fact]
        box_office_fees_list = [box_office_fees.put_into_dto() for box_office_fees in self.box_office_fees]
        review_list = [review.put_into_dto() for review in self.ratings]
        film_actors = [film_actors.put_into_dto() for film_actors in self.film_association]

        return {
            "id": self.id,
            "name": self.name,
            "rating_list": rating_list,
            "fact_list": fact_list,
            "box_office_fees_list": box_office_fees_list,
            "review_list": review_list,
            "film_actors": film_actors,



            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Film(
            name=dto_dict.get("name"),
            rating_list =dto_dict.get("rating_list"),
            fact_list = dto_dict.get("fact_list"),
            box_office_fees_list=dto_dict.get("box_office_fees_list"),
            review_list=dto_dict.get("review_list"),
            film_actors=dto_dict.get("film_actors"),
        )
        return obj
