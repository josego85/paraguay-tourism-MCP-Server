"""Service for location-based calculations and distance operations."""

import math
from typing import List, Tuple

from ..models import Place


class LocationService:
    """Service for calculating distances and location-based operations."""

    # Earth's radius in kilometers
    EARTH_RADIUS_KM = 6371.0

    @staticmethod
    def calculate_distance_km(
        lat1: float, lng1: float, lat2: float, lng2: float
    ) -> float:
        """
        Calculate the distance between two geographic points using the Haversine formula.

        Args:
            lat1: Latitude of the first point in decimal degrees.
            lng1: Longitude of the first point in decimal degrees.
            lat2: Latitude of the second point in decimal degrees.
            lng2: Longitude of the second point in decimal degrees.

        Returns:
            Distance in kilometers between the two points.
        """
        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(lat1)
        lng1_rad = math.radians(lng1)
        lat2_rad = math.radians(lat2)
        lng2_rad = math.radians(lng2)

        # Difference in coordinates
        dlat = lat2_rad - lat1_rad
        dlng = lng2_rad - lng1_rad

        # Haversine formula
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1_rad)
            * math.cos(lat2_rad)
            * math.sin(dlng / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distance in kilometers
        distance = LocationService.EARTH_RADIUS_KM * c
        return distance

    @staticmethod
    def filter_places_by_distance(
        places: List[Place],
        center_lat: float,
        center_lng: float,
        max_distance_km: float,
    ) -> List[Tuple[Place, float]]:
        """
        Filter places within a specified distance from a center point.

        Args:
            places: List of Place models to filter.
            center_lat: Latitude of the center point in decimal degrees.
            center_lng: Longitude of the center point in decimal degrees.
            max_distance_km: Maximum distance in kilometers from the center point.

        Returns:
            List of tuples containing (Place, distance_km) sorted by distance (closest first).
        """
        results = []
        for place in places:
            distance = LocationService.calculate_distance_km(
                center_lat, center_lng, place.lat, place.lng
            )
            if distance <= max_distance_km:
                results.append((place, distance))

        # Sort by distance (closest first)
        results.sort(key=lambda x: x[1])
        return results

