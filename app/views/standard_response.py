# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the StandardResponse class, a helper for creating
consistent and structured HTTP responses in Flask APIs.

It wraps response content in a standardized format using the APIResponse model
and returns it as a Flask-compatible JSON response.
"""

from typing import Any, Dict, Optional, Tuple

from flask import Response, jsonify

from ..models import APIResponse


class StandardResponse:
    """
    A class to create standardized API responses for Flask applications.

    Attributes:
        response (APIResponse): The response payload following a consistent structure.
        status_code (int): HTTP status code to return (default is 200).
    """

    def __init__(
        self,
        success: bool,
        message: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        status_code: int = 200,
    ):
        """
        Initializes the StandardResponse object.

        Args:
            success (bool): Indicates whether the request was successful.
            message (str, optional): Informative message about the response.
            data (dict, optional): Payload data to return to the client.
            status_code (int, optional): HTTP status code (default is 200).
        """
        self.response: APIResponse = APIResponse(success, message or "", data)
        self.status_code = status_code

    def __call__(self) -> Tuple[Response, int]:
        """
        Serializes the response into a Flask-compatible JSON response.

        Returns:
            Tuple[Response, int]: A Flask Response object with a JSON body and status code.
        """
        return jsonify(self.response.to_json()), self.status_code
