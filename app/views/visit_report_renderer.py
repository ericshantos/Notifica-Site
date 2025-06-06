# -*- coding: utf-8 -*-
"""
@Author: Eric dos Santos (ericshantos13@gmail.com)

This module provides functionality for generating HTML reports based on
daily visit data received by a portfolio. Its main responsibility is to
render the data in a clear and user-friendly visual format.
"""

import html

from ..models import VisitReport


class VisitReportRenderer:
    """
    Class responsible for rendering an HTML report from a VisitReport instance
    containing access data for a specific day.
    """

    @classmethod
    def render(cls, report: VisitReport) -> str:
        """
        Renders an HTML report based on the data provided by a VisitReport object.

        Args:
            report (VisitReport): Object containing the date, total visit count,
            and a log of visit times and their counts.

        Returns:
            str: A string containing the HTML content of the daily access report.
        """

        # Generate the list of visit times if any logs are available
        if report.log:
            items = "".join(
                f"<li>{html.escape(str(hour))} → {html.escape(str(visits))} visit(s)</li>"
                for hour, visits in sorted(report.log.items())
            )
            time_list_html = f"<ul>{items}</ul>"
        else:
            # Default message if no visits were logged
            time_list_html = "<p>No visits recorded today.</p>"

        # Escape sensitive values to prevent HTML injection
        count = html.escape(str(report.count))
        date = report.date.strftime("%d/%m/%Y")

        # Build and return the final HTML content
        return f"""
        <html>
        <head><title>Daily Report</title></head>
        <body>
            <p>Your portfolio received <strong>{count}</strong> visit(s) today! 🤩🙏</p>
            <p>Daily access report - {date}</p>
            <p><strong>Visit times:</strong></p>
            {time_list_html}
            <img src="GIF OR IMAGE" alt="Visit chart">
        </body>
        </html>
        """
