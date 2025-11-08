"""Repository for accessing place data."""

import json
from pathlib import Path
from typing import List, Optional

from ..models import Place


class PlaceRepository:
    """Repository for managing place data access."""

    def __init__(self, data_path: str | Path | None = None):
        """
        Initialize the repository.

        Args:
            data_path: Path to the places.json file. If None, uses default path.
        """
        if data_path is None:
            # Default to data/places.json relative to project root
            project_root = Path(__file__).parent.parent.parent.parent
            self._data_path = project_root / "data" / "places_germany.json"
        else:
            self._data_path = Path(data_path)

    def get_all(self) -> List[Place]:
        """
        Retrieve all places from the data source.

        Returns:
            List of Place models.

        Raises:
            FileNotFoundError: If the data file doesn't exist.
            ValueError: If the data is invalid.
        """
        if not self._data_path.exists():
            raise FileNotFoundError(f"Data file not found: {self._data_path}")

        with open(self._data_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Invalid data format: expected a list")

        return [Place(**place) for place in data]

    def get_by_id(self, place_id: str) -> Optional[Place]:
        """
        Retrieve a place by its ID.

        Args:
            place_id: The ID of the place to retrieve.

        Returns:
            Place model if found, None otherwise.

        Raises:
            FileNotFoundError: If the data file doesn't exist.
            ValueError: If the data is invalid.
        """
        places = self.get_all()
        for place in places:
            if place.id == place_id:
                return place
        return None

