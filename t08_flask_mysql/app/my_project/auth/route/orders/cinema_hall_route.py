"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import cinema_hall_controller
from t08_flask_mysql.app.my_project.auth.domain import Cinema_hall

cinema_hall_bp = Blueprint('cinema_hall', __name__, url_prefix='/cinema_hall')


@cinema_hall_bp.get('')
def get_all_cinema_hall() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(cinema_hall_controller.find_all()), HTTPStatus.OK)


@cinema_hall_bp.post('')
def create_cinema_hall() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    cinema_hall = Cinema_hall.create_from_dto(content)
    cinema_hall_controller.create(cinema_hall)
    return make_response(jsonify(cinema_hall.put_into_dto()), HTTPStatus.CREATED)


@cinema_hall_bp.get('/<int:cinema_hall_id>')
def get_cinema_hall(cinema_hall_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(cinema_hall_controller.find_by_id(cinema_hall_id)), HTTPStatus.OK)


@cinema_hall_bp.put('/<int:cinema_hall_id>')
def update_cinema_hall(cinema_hall_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    cinema_hall = Cinema_hall.create_from_dto(content)
    cinema_hall_controller.update(cinema_hall_id, cinema_hall)
    return make_response("Cinema_hall updated", HTTPStatus.OK)


@cinema_hall_bp.patch('/<int:cinema_hall_id>')
def patch_cinema_hall(cinema_hall_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    cinema_hall_controller.patch(cinema_hall_id, content)
    return make_response("Cinema_hall updated", HTTPStatus.OK)


@cinema_hall_bp.delete('/<int:cinema_hall_id>')
def delete_cinema_hall(cinema_hall_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    cinema_hall_controller.delete(cinema_hall_id)
    return make_response("Cinema_hall deleted", HTTPStatus.OK)
