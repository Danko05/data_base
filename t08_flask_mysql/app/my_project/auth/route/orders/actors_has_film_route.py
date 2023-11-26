"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import actors_has_film_controller
from t08_flask_mysql.app.my_project.auth.domain import Actors_has_film

actors_has_film_bp = Blueprint('actors_has_film', __name__, url_prefix='/actors_has_film')


@actors_has_film_bp.get('')
def get_all_actors_has_filmr() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(actors_has_film_controller.find_all()), HTTPStatus.OK)


@actors_has_film_bp.post('')
def create_actors_has_film() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    actors_has_film = Actors_has_film.create_from_dto(content)
    actors_has_film_controller.create(actors_has_film)
    return make_response(jsonify(actors_has_film.put_into_dto()), HTTPStatus.CREATED)


@actors_has_film_bp.get('/<int:actors_has_film_id>')
def get_actors_has_film(actors_has_film_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(actors_has_film_controller.find_by_id(actors_has_film_id)), HTTPStatus.OK)


@actors_has_film_bp.put('/<int:actors_has_film_id>')
def update_actors_has_film(actors_has_film_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    actors_has_film = Actors_has_film.create_from_dto(content)
    actors_has_film_controller.update(actors_has_film_id, actors_has_film)
    return make_response("Film_has_viewer updated", HTTPStatus.OK)


@actors_has_film_bp.patch('/<int:actors_has_film_id>')
def patch_actors_has_film(actors_has_film_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    actors_has_film_controller.patch(actors_has_film_id, content)
    return make_response("actors_has_film updated", HTTPStatus.OK)


@actors_has_film_bp.delete('/<int:actors_has_film_id>')
def delete_actors_has_film(actors_has_film_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    actors_has_film_controller.delete(actors_has_film_id)
    return make_response("cinema_has_viewer deleted", HTTPStatus.OK)
