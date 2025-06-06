# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module initializes the 'home' router using the Router class,
registering routes related to the homepage or root URL.

Routes:
    - GET / : mapped to HomeController.welcome
"""

from ..controllers import HomeController
from .router import Router

router = Router(__name__, "home", url_prefix="/")

router.add_controller("/", HomeController.welcome, methods=["GET"])
