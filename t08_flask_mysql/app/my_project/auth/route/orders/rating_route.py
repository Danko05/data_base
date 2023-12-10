"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import rating_controller
from t08_flask_mysql.app.my_project.auth.domain import Rating

rating_bp = Blueprint('rating', __name__, url_prefix='/rating')


@rating_bp.get('')
def get_all_rating() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(rating_controller.find_all()), HTTPStatus.OK)


@rating_bp.post('')
def create_rating() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    rating = Rating.create_from_dto(content)
    rating_controller.create(rating)
    return make_response(jsonify(rating.put_into_dto()), HTTPStatus.CREATED)


@rating_bp.get('/<int:rating_id>')
def get_rating(rating_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(rating_controller.find_by_id(rating_id)), HTTPStatus.OK)


@rating_bp.put('/<int:rating_id>')
def update_rating(rating_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    rating = Rating.create_from_dto(content)
    rating_controller.update(rating_id, rating)
    return make_response("Rating updated", HTTPStatus.OK)


@rating_bp.patch('/<int:rating_id>')
def patch_rating(rating_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    rating_controller.patch(rating_id, content)
    return make_response("Rating updated", HTTPStatus.OK)


@rating_bp.delete('/<int:rating_id>')
def delete_rating(rating_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    rating_controller.delete(rating_id)
    return make_response("Rating deleted", HTTPStatus.OK)


@rating_bp.post('/CallGetMaxRating')
def CallGetMaxRating() -> Response:

    result = rating_controller.CallGetMaxRating()
    return make_response(jsonify(result), HTTPStatus.OK)
