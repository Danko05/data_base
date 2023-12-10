"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import viewer_controller
from t08_flask_mysql.app.my_project.auth.domain import Viewer

viewer_bp = Blueprint('viewer', __name__, url_prefix='/viewer')


@viewer_bp.get('')
def get_all_viewer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(viewer_controller.find_all()), HTTPStatus.OK)


@viewer_bp.post('')
def create_viewer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    viewer = Viewer.create_from_dto(content)
    viewer_controller.create(viewer)
    return make_response(jsonify(viewer.put_into_dto()), HTTPStatus.CREATED)


@viewer_bp.get('/<int:viewer_id>')
def get_viewer(viewer_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(viewer_controller.find_by_id(viewer_id)), HTTPStatus.OK)


@viewer_bp.put('/<int:viewer_id>')
def update_viewer(viewer_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    viewer = Viewer.create_from_dto(content)
    viewer_controller.update(viewer_id, viewer)
    return make_response("Viewer updated", HTTPStatus.OK)


@viewer_bp.patch('/<int:viewer_id>')
def patch_viewer(viewer_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    viewer_controller.patch(viewer_id, content)
    return make_response("Viewer updated", HTTPStatus.OK)


@viewer_bp.delete('/<int:viewer_id>')
def delete_viewer(viewer_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    viewer_controller.delete(viewer_id)
    return make_response("Viewer deleted", HTTPStatus.OK)


@viewer_bp.post('/InsertRandomTables')
def InsertRandomTables() -> Response:


    result = viewer_controller.InsertRandomTables()
    return make_response(jsonify(result), HTTPStatus.OK)