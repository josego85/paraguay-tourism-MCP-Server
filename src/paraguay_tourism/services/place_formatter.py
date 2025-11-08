"""Service for formatting place data."""

from typing import Dict, List, Optional

from tabulate import tabulate

from ..models import Place


class PlaceFormatter:
    """Service for formatting place data into different representations."""

    @staticmethod
    def format_as_table(places: List[Place]) -> str:
        """
        Format places as a table.

        Args:
            places: List of Place models to format.

        Returns:
            Formatted table string.
        """
        table_data = [
            [place.name, place.city, place.category, f"{place.lat}, {place.lng}"]
            for place in places
        ]
        headers = ["Lugar", "Ciudad", "Categoría", "Lat, lng"]
        return tabulate(table_data, headers=headers, tablefmt="grid")

    @staticmethod
    def format_as_dict(places: List[Place]) -> Dict:
        """
        Format places as a dictionary with table and raw data.

        Args:
            places: List of Place models to format.

        Returns:
            Dictionary with total count, formatted table, and raw data.
        """
        return {
            "total": len(places),
            "table": PlaceFormatter.format_as_table(places),
            "raw": [place.model_dump() for place in places],
        }

    @staticmethod
    def format_single(place: Optional[Place]) -> Dict:
        """
        Format a single place as a dictionary.

        Args:
            place: Place model to format, or None if not found.

        Returns:
            Dictionary with place data, or error message if not found.
        """
        if place is None:
            return {
                "found": False,
                "message": "Lugar turístico no encontrado",
            }

        return {
            "found": True,
            "place": place.model_dump(),
        }

    @staticmethod
    def format_with_distances(places_with_distances: List[tuple]) -> Dict:
        """
        Format places with their distances as a dictionary.

        Args:
            places_with_distances: List of tuples (Place, distance_km).

        Returns:
            Dictionary with total count, formatted table with distances, and raw data.
        """
        if not places_with_distances:
            return {
                "total": 0,
                "table": "No se encontraron lugares en el rango especificado.",
                "raw": [],
            }

        table_data = [
            [
                place.name,
                place.city,
                place.category,
                f"{place.lat}, {place.lng}",
                f"{distance:.2f} km",
            ]
            for place, distance in places_with_distances
        ]
        headers = ["Lugar", "Ciudad", "Categoría", "Coordenadas", "Distancia"]
        table = tabulate(table_data, headers=headers, tablefmt="grid")

        return {
            "total": len(places_with_distances),
            "table": table,
            "raw": [
                {**place.model_dump(), "distance_km": round(distance, 2)}
                for place, distance in places_with_distances
            ],
        }

