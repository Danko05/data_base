"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Cinema(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "cinema"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    ticket_price = db.Column(db.Integer)
    max_seats = db.Column(db.Integer)
    midlle_age_viewer = db.Column(db.Float)
    films_association = db.relationship("Film_has_cinema", backref="cinema")



    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.name}', '{self.ticket_price}', '{self.max_seats}', '{self.midlle_age_viewer}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        cinema_films = [cinema_films.put_into_dto() for cinema_films in self.films_association]
        return {
            "id": self.id,
            "name": self.name,
            "ticket_price": self.ticket_price,
            "max_seats": self.max_seats,
            "midlle_age_viewer": self.midlle_age_viewer,
            "cinema_films": cinema_films,
            # "client_type_id": self.client_type_id or "",
            # "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Cinema:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Cinema(
            name=dto_dict.get("name"),
            ticket_price=dto_dict.get("ticket_price"),
            max_seats=dto_dict.get("max_seats"),
            midlle_age_viewer=dto_dict.get("midlle_age_viewer"),
            cinema_films=dto_dict.get("cinema_films"),
        )
        return obj
