from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class APIResponse:
    """
    Represents a standardized API response structure.

    Attributes:
        success (bool): Indicates if the API request was successful.
        message (str): A human-readable message describing the response.
        data (Optional[Dict[str, Any]]): Optional additional data payload.
    """

    success: bool
    message: str
    data: Optional[Dict[str, Any]]

    def to_json(self) -> Dict[str, Any]:
        """
        Converts the APIResponse instance into a JSON-serializable dictionary,
        excluding any fields with a value of None.

        Returns:
            Dict[str, Any]: The dictionary representation of the response.
        """
        response_dict = {
            "success": self.success,
            "message": self.message,
            "data": self.data,
        }

        # Remove keys with None values to keep the response clean
        return {k: v for k, v in response_dict.items() if v is not None}
