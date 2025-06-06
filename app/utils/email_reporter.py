# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module defines the EmailReporter class, which is responsible for
creating and sending a daily visit report as an HTML email.

It integrates data modeling (VisitReport), rendering (VisitReportRenderer),
and email delivery (EmailSender via EmailNotificator).
"""

from datetime import datetime

from ..models import VisitReport
from ..views import VisitReportRenderer
from .email_notificator import EmailNotificator


class EmailReporter:
    """
    Class responsible for composing and sending the daily visit report via email.

    It uses the VisitReport model to structure the data,
    VisitReportRenderer to create the HTML content,
    and EmailSender to deliver the message.
    """

    def __init__(self):
        """
        Initializes the EmailReporter and sets up the email sender using
        the default configuration provided by EmailNotificator.
        """
        self.email_sender = EmailNotificator().email_sender

    def send(self, count: int, log: dict) -> None:
        """
        Composes the visit report and sends it as an HTML email.

        Args:
            count (int): Total number of visits.
            log (dict): Dictionary of visits grouped by time (e.g., {"14h": 5}).
        """
        try:
            report = VisitReport(count, log, datetime.now())
            html = VisitReportRenderer.render(report)

            self.email_sender.send_html(
                to_address=self.email_sender.email_address,
                subject="Relatório diário de visitas",
                html=html,
            )
        except Exception as e:
            print(f"[❌] Erro ao enviar relatório: {e}")
