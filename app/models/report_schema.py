from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class VisitReport:
    """
    Data class representing a visit report summary.

    Attributes:
        count (int): Total number of visits.
        log (Dict[str, int]): Dictionary mapping
        time (e.g., hour) to number of visits.
        date (datetime): Date of the report.
    """

    count: int
    log: Dict[str, int]
    date: datetime
