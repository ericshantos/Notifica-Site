# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Module providing a base controller to standardize
request handling and response formatting in the
application.
"""

from typing import Any, Callable, Tuple

from flask import Response

from ..views import StandardResponse


class BaseController:
    """
    Base controller class that provides a standardized
    method to handle service method calls and generate
    API responses.
    """

    @staticmethod
    def handle_request(
        service_method: Callable[..., Any], *args, **kwargs
    ) -> Tuple[Response, int]:
        """
        Executes the given service method with provided
        arguments, returning a standardized JSON response.

        Args:
            service_method (Callable): The service function/method to execute.
            *args: Positional arguments for the service method.
            **kwargs: Keyword arguments for the service method.

        Returns:
            Response: Flask Response object with JSON data and HTTP status code.
        """
        try:
            result = service_method(*args, **kwargs)
            return StandardResponse(success=True, data=result)()
        except Exception as e:
            return StandardResponse(success=False, message=str(e), status_code=400)()
