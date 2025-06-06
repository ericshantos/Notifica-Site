# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Application factory module to create and configure the Flask app instance,
including initializing scheduler, enabling CORS, and registering routers.
"""

from flask import Flask
from flask_cors import CORS

from .routers import home_router
from .utils import scheduler


class AppFactory:
    """
    Factory class for creating and configuring the Flask application.
    """

    def __init__(self, env_config: str = "dev"):
        """
        Initializes the factory with environment configuration.

        Args:
            env_config (str): Environment configuration name,
            e.g. "dev", "prod".
        """
        self.env_config = env_config

    def __call__(self) -> Flask:
        """
        Creates and configures the Flask application instance.

        Returns:
            Flask: Configured Flask application.
        """
        app = Flask(__name__)

        # Start the visit reporting scheduler
        scheduler.start()

        # Enable Cross-Origin Resource Sharing (CORS)
        CORS(app)

        # Register blueprints (routers)
        home_router.to(app)

        return app
