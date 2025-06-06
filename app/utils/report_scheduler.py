# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the ReportScheduler class, which automates the daily sending
of visit reports using a separate background thread.

The scheduler calculates the wait time until the next scheduled report,
sends the report via an EmailReporter, and resets the visit data afterward.
"""

import logging
import threading
import time as time_module
from datetime import datetime, time, timedelta
from typing import Optional

from .email_reporter import EmailReporter
from .visit_tracker import VisitTracker

logger = logging.getLogger(__name__)


class ReportScheduler:
    """
    A scheduler responsible for sending daily visit reports at a specified time.

    This class runs a background thread that waits until the scheduled time,
    triggers the report generation, and clears the visit data afterward.
    """

    def __init__(
        self,
        visit_tracker: VisitTracker,
        report_time: time = time(18, 0),
        reporter: Optional[EmailReporter] = None,
    ):
        """
        Initializes the report scheduler.

        Args:
            visit_tracker (VisitTracker): Instance responsible for tracking visits.
            report_time (datetime.time): Time of day to send the report (default is 18:00).
            reporter (EmailReporter, optional): Instance responsible for sending the report.
            If None, a default EmailReporter is created.
        """
        self.visit_tracker = visit_tracker
        self.report_time = report_time
        self.report_sender = reporter or EmailReporter()
        self.thread = threading.Thread(target=self._run, daemon=True)
        self._stop_event = threading.Event()

    def start(self) -> None:
        """
        Starts the scheduler in a background daemon thread if not already running.
        """
        if not self.thread.is_alive():
            self.thread.start()

    def _calculate_wait_seconds(self) -> float:
        """
        Calculates the number of seconds to wait until the next report time.

        Returns:
            float: Time to wait in seconds until the next scheduled report.
        """
        now = datetime.now()
        target = datetime.combine(now.date(), self.report_time)

        # If the target time today has already passed, schedule for tomorrow
        if now > target:
            target += timedelta(days=1)

        return (target - now).total_seconds()

    def _run(self) -> None:
        """
        Main loop that waits until the scheduled time, sends the report,
        and resets the visit data. The loop repeats daily unless interrupted.
        """
        while True:
            wait_seconds = self._calculate_wait_seconds()
            logger.info(
                f"[Scheduler] Next report at {self.report_time.strftime('%H:%M')}. Waiting {wait_seconds:.0f} seconds..."
            )
            time_module.sleep(wait_seconds)

            self._send_report()
            self.visit_tracker._reset_data()

            if self._stop_event.wait(timeout=wait_seconds):
                break

    def _send_report(self) -> None:
        """
        Attempts to send the visit report using the configured EmailReporter.
        Logs any exceptions encountered.
        """
        try:
            logger.info("[Scheduler] Sending report...")
            self.report_sender.send(
                self.visit_tracker.total_accesses, self.visit_tracker.visit_log
            )
        except Exception as e:
            logger.error(f"[Scheduler] Failed to send report: {e}")
