"""Dependency Injection Container for managing application dependencies."""

from ..repositories import PlaceRepository
from ..services import GeolocationService, LocationService, PlaceFormatter


class DependencyContainer:
    """Container for managing and providing application dependencies."""

    def __init__(self):
        """Initialize all dependencies."""
        self._place_repository: PlaceRepository | None = None
        self._place_formatter: PlaceFormatter | None = None
        self._location_service: LocationService | None = None
        self._geolocation_service: GeolocationService | None = None

    @property
    def place_repository(self) -> PlaceRepository:
        """Get or create PlaceRepository instance."""
        if self._place_repository is None:
            self._place_repository = PlaceRepository()
        return self._place_repository

    @property
    def place_formatter(self) -> PlaceFormatter:
        """Get or create PlaceFormatter instance."""
        if self._place_formatter is None:
            self._place_formatter = PlaceFormatter()
        return self._place_formatter

    @property
    def location_service(self) -> LocationService:
        """Get or create LocationService instance."""
        if self._location_service is None:
            self._location_service = LocationService()
        return self._location_service

    @property
    def geolocation_service(self) -> GeolocationService:
        """Get or create GeolocationService instance."""
        if self._geolocation_service is None:
            self._geolocation_service = GeolocationService()
        return self._geolocation_service


# Singleton instance
_container: DependencyContainer | None = None


def get_container() -> DependencyContainer:
    """
    Get the global dependency container instance (singleton pattern).
    
    Returns:
        DependencyContainer instance.
    """
    global _container
    if _container is None:
        _container = DependencyContainer()
    return _container

