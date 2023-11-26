"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import box_office_fees_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class Box_office_feesController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = box_office_fees_service
