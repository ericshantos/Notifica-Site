# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This package provides tools for handling visit data and generating
standardized HTML reports.

Modules:
- standard_response: Defines a generic response structure used across the application.
- visit_report_renderer: Provides functionality to render HTML reports from visit data.

Exports:
- StandardResponse: A standard response wrapper for API output or internal messaging.
- VisitReportRenderer: Responsible for generating HTML reports from visit logs.
"""

from .standard_response import StandardResponse
from .visit_report_renderer import VisitReportRenderer

__all__ = ["StandardResponse", "VisitReportRenderer"]
__author__ = "Eric Santos <ericshantos13@gmail.com>"
