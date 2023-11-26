"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import facts_controller
from t08_flask_mysql.app.my_project.auth.domain import Facts

facts_bp = Blueprint('facts', __name__, url_prefix='/facts')


@facts_bp.get('')
def get_all_facts() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(facts_controller.find_all()), HTTPStatus.OK)


@facts_bp.post('')
def create_facts() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    facts = Facts.create_from_dto(content)
    facts_controller.create(facts)
    return make_response(jsonify(facts.put_into_dto()), HTTPStatus.CREATED)


@facts_bp.get('/<int:facts_id>')
def get_facts(facts_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(facts_controller.find_by_id(facts_id)), HTTPStatus.OK)


@facts_bp.put('/<int:facts_id>')
def update_facts(facts_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    facts = Facts.create_from_dto(content)
    facts_controller.update(facts_id, facts)
    return make_response("Facts updated", HTTPStatus.OK)


@facts_bp.patch('/<int:facts_id>')
def patch_facts(facts_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    facts_controller.patch(facts_id, content)
    return make_response("Facts updated", HTTPStatus.OK)


@facts_bp.delete('/<int:facts_id>')
def delete_facts(facts_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    facts_controller.delete(facts_id)
    return make_response("Facts deleted", HTTPStatus.OK)
