# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the VisitTracker class, which is responsible
for safely tracking and logging HTTP endpoint visits in a
multi-threaded environment.

It provides synchronized methods for logging and retrieving
visit counts, and includes a mechanism to reset the data
periodically (e.g., by a scheduler).
"""

import logging
from collections import defaultdict
from threading import Lock
from typing import Dict

logger = logging.getLogger(__name__)


class VisitTracker:
    """
    Tracks total access counts and per-endpoint visits
    using thread-safe operations.

    This class is suitable for use in multi-threaded web
    applications where accurate logging of endpoint
    usage is needed.
    """

    def __init__(self) -> None:
        """
        Initializes a VisitTracker instance with internal
        counters and thread lock.
        """
        self._access_count = 0
        self._visit_log: Dict[str, int] = defaultdict(int)
        self.lock = Lock()

    def log_visit(self, endpoint: str) -> None:
        """
        Records a visit to the specified endpoint.

        Args:
            endpoint (str): The path or name of the
            endpoint being accessed.
        """
        with self.lock:
            self._access_count += 1
            self._visit_log[endpoint] += 1

        logger.info(f"Visit logged for endpoint '{endpoint}'")

    def get_visits(self, endpoint: str) -> int:
        """
        Retrieves the number of visits for a specific endpoint.

        Args:
            endpoint (str): The name of the endpoint.

        Returns:
            int: Number of visits to the given endpoint.
        """
        with self.lock:
            return self._visit_log.get(endpoint, 0)

    def _reset_data(self) -> None:
        """
        Resets all stored visit data (used by schedulers or
        manual maintenance).
        """
        logger.info("[Scheduler] Resetting visit data.")

        with self.lock:
            self._access_count = 0
            self._visit_log = defaultdict(int)

    @property
    def total_accesses(self) -> int:
        """
        Returns:
            int: The total number of accesses across all endpoints.
        """
        return self._access_count

    @property
    def visit_log(self) -> Dict[str, int]:
        """
        Returns:
            dict: A dictionary with endpoint names as keys and
            visit counts as values.
        """
        with self.lock:
            return dict(self._visit_log)
