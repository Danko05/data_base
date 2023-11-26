"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from t08_flask_mysql.app.my_project.auth.domain.orders.facts import Facts
from t08_flask_mysql.app.my_project.auth.domain.orders.actor import Actors
from t08_flask_mysql.app.my_project.auth.domain.orders.cinema import Cinema
from t08_flask_mysql.app.my_project.auth.domain.orders.viewer import Viewer
from t08_flask_mysql.app.my_project.auth.domain.orders.rating import Rating
from t08_flask_mysql.app.my_project.auth.domain.orders.film import Film
from t08_flask_mysql.app.my_project.auth.domain.orders.box_office_fees import Box_office_fees
from t08_flask_mysql.app.my_project.auth.domain.orders.review import Review
from t08_flask_mysql.app.my_project.auth.domain.orders.film_has_viewer import Film_has_viewer
from t08_flask_mysql.app.my_project.auth.domain.orders.cinema_has_viewer import Cinema_has_viewer
from t08_flask_mysql.app.my_project.auth.domain.orders.film_has_cinema import Film_has_cinema
from t08_flask_mysql.app.my_project.auth.domain.orders.actors_has_film import Actors_has_film
