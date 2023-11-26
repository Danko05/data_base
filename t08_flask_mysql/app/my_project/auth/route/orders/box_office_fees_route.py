"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import box_office_fees_controller
from t08_flask_mysql.app.my_project.auth.domain import Box_office_fees

box_office_fees_bp = Blueprint('box_office_fees', __name__, url_prefix='/box_office_fees')


@box_office_fees_bp.get('')
def get_all_facts() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(box_office_fees_controller.find_all()), HTTPStatus.OK)


@box_office_fees_bp.post('')
def create_facts() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    box_office_fees = Box_office_fees.create_from_dto(content)
    box_office_fees_controller.create(box_office_fees)
    return make_response(jsonify(box_office_fees.put_into_dto()), HTTPStatus.CREATED)


@box_office_fees_bp.get('/<int:box_office_fees_id>')
def get_facts(box_office_fees_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(box_office_fees_controller.find_by_id(box_office_fees_id)), HTTPStatus.OK)


@box_office_fees_bp.put('/<int:box_office_fees_id>')
def update_box_office_fees(box_office_fees_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    box_office_fees = Box_office_fees.create_from_dto(content)
    box_office_fees_controller.update(box_office_fees_id, box_office_fees)
    return make_response("Facts updated", HTTPStatus.OK)


@box_office_fees_bp.patch('/<int:box_office_fees_id>')
def patch_box_office_fees(box_office_fees_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    box_office_fees_controller.patch(box_office_fees_id, content)
    return make_response("Box_office_fees updated", HTTPStatus.OK)


@box_office_fees_bp.delete('/<int:box_office_fees_id>')
def delete_box_office_fees(box_office_fees_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    box_office_fees_controller.delete(box_office_fees_id)
    return make_response("Box_office_fees deleted", HTTPStatus.OK)
