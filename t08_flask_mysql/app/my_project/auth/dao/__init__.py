"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.facts_dao import FactsDAO
from .orders.actor_dao import ActorDAO
from .orders.cinema_dao import CinemaDAO
from .orders.viewer_dao import ViewerDAO
from .orders.rating_dao import RatingDAO
from .orders.film_dao import FilmDAO
from .orders.box_office_fees_dao import Box_office_feesDAO
from .orders.review_dao import ReviewDAO
from .orders.film_has_viewer_dao import Film_has_viewerDAO
from .orders.cinema_has_viewer_dao import Cinema_has_viewerDAO
from .orders.film_has_cinema_dao import Film_has_cinemaDAO
from .orders.actors_has_film_dao import Actors_has_filmDAO
from .orders.cinema_hall_dao import Cinema_hallDAO


facts_dao = FactsDAO()
actor_dao = ActorDAO()
cinema_dao = CinemaDAO()
viewer_dao = ViewerDAO()
rating_dao = RatingDAO()
film_dao = FilmDAO()
box_office_fees_dao = Box_office_feesDAO()
review_dao = ReviewDAO()
film_has_viewer_dao = Film_has_viewerDAO()
cinema_has_viewer_dao = Cinema_has_viewerDAO()
film_has_cinema_dao = Film_has_cinemaDAO()
actors_has_film_dao = Actors_has_filmDAO()
cinema_hall_dao = Cinema_hallDAO()
