"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import cinema_controller
from t08_flask_mysql.app.my_project.auth.domain import Cinema

cinema_bp = Blueprint('cinema', __name__, url_prefix='/cinema')


@cinema_bp.get('')
def get_all_cinema() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(cinema_controller.find_all()), HTTPStatus.OK)


@cinema_bp.post('')
def create_cinema() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    cinema = Cinema.create_from_dto(content)
    cinema_controller.create(cinema)
    return make_response(jsonify(cinema.put_into_dto()), HTTPStatus.CREATED)


@cinema_bp.get('/<int:cinema_id>')
def get_cinema(cinema_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(cinema_controller.find_by_id(cinema_id)), HTTPStatus.OK)


@cinema_bp.put('/<int:cinema_id>')
def update_cinema(cinema_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    cinema = Cinema.create_from_dto(content)
    cinema_controller.update(cinema_id, cinema)
    return make_response("Cinema updated", HTTPStatus.OK)


@cinema_bp.patch('/<int:cinema_id>')
def patch_cinema(cinema_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    cinema_controller.patch(cinema_id, content)
    return make_response("Cinema updated", HTTPStatus.OK)


@cinema_bp.delete('/<int:cinema_id>')
def delete_cinema(cinema_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    cinema_controller.delete(cinema_id)
    return make_response("Cinema deleted", HTTPStatus.OK)
