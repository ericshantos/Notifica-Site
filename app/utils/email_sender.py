# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module provides a simple utility class for sending HTML emails via SMTP.

The EmailSender class encapsulates all necessary configuration and
sending logic, making it reusable for email notification systems.
"""

import smtplib
from email.mime.text import MIMEText


class EmailSender:
    """
    Utility class for sending HTML-formatted emails using SMTP.
    """

    def __init__(
        self, email_address: str, email_password: str, smtp_server: str, smtp_port: int
    ):
        """
        Initializes the EmailSender with SMTP credentials and server configuration.

        Args:
            email_address (str): Sender's email address used to authenticate.
            email_password (str): Password or app-specific token for the email account.
            smtp_server (str): Address of the SMTP server (e.g., smtp.gmail.com).
            smtp_port (int): Port used to connect to the SMTP server (usually 587).
        """
        self.email_address = email_address
        self.email_password = email_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_html(self, to_address: str, subject: str, html: str) -> None:
        """
        Sends an HTML email to the specified recipient.

        Args:
            to_address (str): Recipient's email address.
            subject (str): Subject line of the email.
            html (str): HTML content to be sent as the email body.
        """
        msg = MIMEText(html, "html")
        msg["Subject"] = subject
        msg["To"] = to_address
        msg["From"] = self.email_address

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
