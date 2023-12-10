"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.facts_route import facts_bp
    from .orders.actor_route import actor_bp
    from .orders.cinema_route import cinema_bp
    from .orders.viewer_route import viewer_bp
    from .orders.rating_route import rating_bp
    from .orders.film_route import film_bp
    from .orders.box_office_fees_route import box_office_fees_bp
    from .orders.review_route import review_bp
    from .orders.film_has_viewer_route import film_has_viewer_bp
    from .orders.cinema_has_viewer_route import cinema_has_viewer_bp
    from .orders.film_has_cinema_route import film_has_cinema_bp
    from .orders.actors_has_film_route import actors_has_film_bp
    from .orders.cinema_hall_route import cinema_hall_bp

    app.register_blueprint(facts_bp)
    app.register_blueprint(actor_bp)
    app.register_blueprint(cinema_bp)
    app.register_blueprint(viewer_bp)
    app.register_blueprint(rating_bp)
    app.register_blueprint(film_bp)
    app.register_blueprint(box_office_fees_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(film_has_viewer_bp)
    app.register_blueprint(cinema_has_viewer_bp)
    app.register_blueprint(film_has_cinema_bp)
    app.register_blueprint(actors_has_film_bp)
    app.register_blueprint(cinema_hall_bp)