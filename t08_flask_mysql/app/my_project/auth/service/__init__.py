"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.facts_service import FactsService
from .orders.actor_service import ActorService
from .orders.cinema_service import CinemaService
from .orders.viewer_service import ViewerService
from .orders.rating_service import RatingService
from .orders.film_service import FilmService
from .orders.box_office_fees_service import Box_office_feesService
from .orders.review_service import ReviewService
from .orders.film_has_viewer_service import Film_has_viewerService
from .orders.cinema_has_viewer_service import Cinema_has_viewerService
from .orders.film_has_cinema_service import Film_has_cinemaService
from .orders.actors_has_film_service import Actors_has_filmService


facts_service = FactsService()
actor_service = ActorService()
cinema_service = CinemaService()
viewer_service = ViewerService()
rating_service = RatingService()
film_service = FilmService()
box_office_fees_service = Box_office_feesService()
review_service = ReviewService()
film_has_viewer_service = Film_has_viewerService()
cinema_has_viewer_service = Cinema_has_viewerService()
film_has_cinema_service = Film_has_cinemaService()
actors_has_film_service =Actors_has_filmService()
