# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the EmailNotificator class, which is responsible for
initializing and providing a configured instance of EmailSender using
environment variables.
"""

from .email_sender import EmailSender
from .env_loader import EnvLoader


class EmailNotificator:
    """
    Responsible for initializing the EmailSender using configuration values
    retrieved from environment variables.

    Environment variables expected:
        - EMAIL_ADDRESS
        - EMAIL_PASSWORD
        - SMTP_SERVER
        - SMTP_PORT
    """

    def __init__(self):
        """
        Loads required email configuration from environment variables
        and initializes the EmailSender instance.
        """
        self._loader = EnvLoader(
            "EMAIL_ADDRESS", "EMAIL_PASSWORD", "SMTP_SERVER", "SMTP_PORT"
        )
        self._email_sender = self._create_email_sender()

    def _create_email_sender(self) -> EmailSender:
        """
        Creates and returns an instance of EmailSender using environment data.

        Returns:
            EmailSender: Configured email sender instance.
        """
        smtp_port = int(self._loader.get("SMTP_PORT", 587))

        return EmailSender(
            email_address=self._loader.get("EMAIL_ADDRESS"),
            email_password=self._loader.get("EMAIL_PASSWORD"),
            smtp_server=self._loader.get("SMTP_SERVER"),
            smtp_port=smtp_port,
        )

    @property
    def email_sender(self) -> EmailSender:
        """
        Returns the initialized EmailSender instance.

        Returns:
            EmailSender: Configured email sender.
        """
        return self._email_sender
