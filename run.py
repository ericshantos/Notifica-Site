"""
Entry point to start the Flask application.

Creates an app instance using AppFactory with production configuration
and runs the Flask development server.
"""

from app import AppFactory

app = AppFactory(env_config="prod")()

if __name__ == "__main__":
    app.run()
