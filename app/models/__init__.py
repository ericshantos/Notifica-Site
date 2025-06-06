# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Package initializer for data models.

Exports:
    - APIResponse: Standardized response data model.
    - VisitReport: Data model summarizing visits and their logs.
"""

from .report_schema import VisitReport
from .responses import APIResponse

__all__ = ["APIResponse", "VisitReport"]

__author__ = "Eric Santos <ericshantos13@gmail.com>"
