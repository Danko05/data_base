"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import film_has_viewer_controller
from t08_flask_mysql.app.my_project.auth.domain import Film_has_viewer

film_has_viewer_bp = Blueprint('film_has_viewer', __name__, url_prefix='/film_has_viewer')


@film_has_viewer_bp.get('')
def get_all_film_has_viewer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(film_has_viewer_controller.find_all()), HTTPStatus.OK)


@film_has_viewer_bp.post('')
def create_film_has_viewer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film_has_viewer = Film_has_viewer.create_from_dto(content)
    film_has_viewer_controller.create(film_has_viewer)
    return make_response(jsonify(film_has_viewer.put_into_dto()), HTTPStatus.CREATED)


@film_has_viewer_bp.get('/<int:film_has_viewer_id>')
def get_film_has_viewer(film_has_viewer_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(film_has_viewer_controller.find_by_id(film_has_viewer_id)), HTTPStatus.OK)


@film_has_viewer_bp.put('/<int:film_has_viewer_id>')
def update_film_has_viewer(film_has_viewer_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    film_has_viewer = Film_has_viewer.create_from_dto(content)
    film_has_viewer_controller.update(film_has_viewer_id, film_has_viewer)
    return make_response("Film_has_viewer updated", HTTPStatus.OK)


@film_has_viewer_bp.patch('/<int:film_has_viewer_id>')
def patch_film_has_viewer(film_has_viewer_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    film_has_viewer_controller.patch(film_has_viewer_id, content)
    return make_response("Film_has_viewer updated", HTTPStatus.OK)


@film_has_viewer_bp.delete('/<int:film_has_viewer_id>')
def delete_film_has_viewer(film_has_viewer_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film_has_viewer_controller.delete(film_has_viewer_id)
    return make_response("Film_has_viewer deleted", HTTPStatus.OK)
