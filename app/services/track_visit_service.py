# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the TrackService class, responsible
for tracking visits to a specific endpoint by delegating
the logging operation to the shared scheduler instance.
"""

from ..utils import scheduler


class TrackService:
    """
    Service class to track visits to a given endpoint.

    Attributes:
        _endpoint (str): The endpoint identifier to be tracked.
    """

    def __init__(self, endpoint: str):
        """
        Initializes the TrackService with the endpoint to be tracked.

        Args:
            endpoint (str): The endpoint path or name to track.
        """
        self._endpoint = endpoint

    def track(self) -> None:
        """
        Logs a visit to the associated endpoint using the global
        scheduler's visit tracker.
        """
        scheduler.visit_tracker.log_visit(self._endpoint)
