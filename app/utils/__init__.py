# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This package initializer sets up and exports a ready-to-use
instance of the ReportScheduler. The scheduler is
responsible for sending daily email reports based on visit
tracking data.

It internally initializes the VisitTracker and EmailReporter
components and wires them together to automate the
reporting process.

Exposed components:
    - scheduler (ReportScheduler): Singleton-like instance
        of the report scheduler.
"""

from .email_reporter import EmailReporter
from .report_scheduler import ReportScheduler
from .visit_tracker import VisitTracker

# Instantiates and configures the daily report scheduler
scheduler = ReportScheduler(visit_tracker=VisitTracker(), reporter=EmailReporter())

__all__ = ["scheduler"]

__author__ = "Eric Santos <ericshantos13@gmail.com>"
