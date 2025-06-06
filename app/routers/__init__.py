# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Package initializer for route modules.

Exports:
    - home_router: Router instance for the home page routes.
"""

from .home_route import router as home_router

__all__ = ["home_router"]

__author__ = "Eric Santos <ericshantos13@gmail.com>"
