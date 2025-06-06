# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the Router class, a thin wrapper
around Flask's Blueprint, designed to facilitate
modular route registration and integration with Flask
applications.
"""

from typing import Callable

from flask import Blueprint, Flask


class Router:
    """
    Router encapsulates a Flask Blueprint to manage
    route definitions and their registration with
    a Flask application.

    Attributes:
        _blueprint (Blueprint): The internal Flask
        Blueprint instance.
    """

    def __init__(self, module: str, name: str, url_prefix: str = ""):
        """
        Initializes the Router with a Flask Blueprint.

        Args:
            module (str): The import name (usually __name__)
                of the module where this router is defined.
            name (str): The name of the blueprint.
            url_prefix (str, optional): The URL prefix for
                all routes in this blueprint.
        """
        self._blueprint = Blueprint(name, module, url_prefix=url_prefix)

    def route(self, rules: str, **options) -> Callable:
        """
        Decorator to define a route on the internal Blueprint.

        Args:
            rules (str): URL rule as string.
            **options: Additional options passed to Blueprint.route().

        Returns:
            Callable: The route decorator.
        """
        return self._blueprint.route(rules, **options)

    def add_controller(self, rule: str, view_func: Callable, **options) -> None:
        """
        Adds a URL rule to the Blueprint programmatically.

        Args:
            rule (str): URL rule as string.
            view_func (Callable): The view function to call for this route.
            **options: Additional options passed to Blueprint.add_url_rule().
        """
        self._blueprint.add_url_rule(rule, view_func=view_func, **options)

    def to(self, app: Flask) -> None:
        """
        Registers the internal Blueprint with a Flask application.

        Args:
            app (Flask): The Flask application instance.
        """
        app.register_blueprint(self._blueprint)

    @property
    def blueprint(self) -> Blueprint:
        """
        Returns the internal Flask Blueprint instance.

        Returns:
            Blueprint: The encapsulated Flask Blueprint.
        """
        return self._blueprint
