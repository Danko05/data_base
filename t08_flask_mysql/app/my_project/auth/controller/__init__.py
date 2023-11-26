"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.facts_controller import FactsController
from .orders.actor_controller import ActorController
from .orders.cinema_controller import CinemaController
from .orders.viewer_controller import ViewerController
from .orders.rating_controller import RatingController
from .orders.film_controller import FilmController
from .orders.box_office_fees_controller import Box_office_feesController
from .orders.review_controller import ReviewController
from .orders.film_has_viewer_controller import Film_has_viewerController
from .orders.cinema_has_viewer_controller import Cinema_has_viewerController
from .orders.film_has_cinema_controller import Film_has_cinemaController
from .orders.actors_has_film_controller import Actors_has_filmController


facts_controller = FactsController()
actor_controller = ActorController()
cinema_controller = CinemaController()
viewer_controller = ViewerController()
rating_controller = RatingController()
film_controller = FilmController()
box_office_fees_controller = Box_office_feesController()
review_controller = ReviewController()
film_has_viewer_controller = Film_has_viewerController()
cinema_has_viewer_controller = Cinema_has_viewerController()
film_has_cinema_controller = Film_has_cinemaController()
actors_has_film_controller = Actors_has_filmController()
