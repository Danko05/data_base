"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import cinema_has_viewer_controller
from t08_flask_mysql.app.my_project.auth.domain import Cinema_has_viewer

cinema_has_viewer_bp = Blueprint('cinema_has_viewer', __name__, url_prefix='/cinema_has_viewer')


@cinema_has_viewer_bp.get('')
def get_all_cinema_has_viewer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(cinema_has_viewer_controller.find_all()), HTTPStatus.OK)


@cinema_has_viewer_bp.post('')
def create_cinema_has_viewer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    cinema_has_viewer = Cinema_has_viewer.create_from_dto(content)
    cinema_has_viewer_controller.create(cinema_has_viewer)
    return make_response(jsonify(cinema_has_viewer.put_into_dto()), HTTPStatus.CREATED)


@cinema_has_viewer_bp.get('/<int:cinema_has_viewer_id>')
def get_cinema_has_viewer(cinema_has_viewer_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(cinema_has_viewer_controller.find_by_id(cinema_has_viewer_id)), HTTPStatus.OK)


@cinema_has_viewer_bp.put('/<int:cinema_has_viewer_id>')
def update_cinema_has_viewer(cinema_has_viewer_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    cinema_has_viewer = Cinema_has_viewer.create_from_dto(content)
    cinema_has_viewer_controller.update(cinema_has_viewer_id, cinema_has_viewer)
    return make_response("Film_has_viewer updated", HTTPStatus.OK)


@cinema_has_viewer_bp.patch('/<int:cinema_has_viewer_id>')
def patch_cinema_has_viewer(cinema_has_viewer_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    cinema_has_viewer_controller.patch(cinema_has_viewer_id, content)
    return make_response("Film_has_viewer updated", HTTPStatus.OK)


@cinema_has_viewer_bp.delete('/<int:cinema_has_viewer_id>')
def delete_cinema_has_viewer(cinema_has_viewer_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    cinema_has_viewer_controller.delete(cinema_has_viewer_id)
    return make_response("cinema_has_viewer deleted", HTTPStatus.OK)
