# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Module containing the HomeController class, responsible for handling
requests to the home route of the application.
"""

from typing import Tuple

from flask import Response

from ..services import TrackService
from .base_controller import BaseController


class HomeController:
    """
    Controller class for handling home page requests.
    """

    @staticmethod
    def welcome() -> Tuple[Response, int]:
        """
        Handles a GET request to the home route by tracking the visit and
        returning a welcome message.

        Returns:
            Tuple[Response, int]: A Flask response object and HTTP status code.
        """

        def hello():
            TrackService(endpoint="home").track()
            return "Olá, seja bem-vindo!"

        return BaseController.handle_request(service_method=hello)
