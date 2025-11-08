"""Handlers for tourist place MCP tools."""

from fastmcp import FastMCP

from ..core.dependencies import DependencyContainer


def register_place_handlers(mcp: FastMCP, container: DependencyContainer) -> None:
    """
    Register all place-related MCP tools.
    
    Args:
        mcp: FastMCP server instance to register tools on.
        container: Dependency container with required services.
    """
    place_repository = container.place_repository
    place_formatter = container.place_formatter
    location_service = container.location_service
    geolocation_service = container.geolocation_service

    @mcp.tool(
        name="list_all_tourist_places",
        description="Lista todos los lugares turísticos de Paraguay con nombre, ciudad, categoría y coordenadas GPS (lat, lng).",
    )
    def list_all_tourist_places() -> dict:
        """
        Retrieve and format all tourist places in Paraguay.

        Returns:
            Dictionary containing total count, formatted table, and raw data.
        """
        places = place_repository.get_all()
        return place_formatter.format_as_dict(places)

    @mcp.tool(
        name="get_tourist_place_by_id",
        description="Obtiene toda la información de un lugar turístico de Paraguay por su ID.",
    )
    def get_tourist_place_by_id(place_id: str) -> dict:
        """
        Retrieve and format a tourist place by its ID.

        Args:
            place_id: The ID of the place to retrieve.

        Returns:
            Dictionary containing place data or error message if not found.
        """
        place = place_repository.get_by_id(place_id)
        return place_formatter.format_single(place)

    @mcp.tool(
        name="find_tourist_places_by_distance",
        description="Busca lugares turísticos de Paraguay dentro de un rango de distancia desde una ubicación específica. Retorna lugares ordenados por distancia (más cercanos primero).",
    )
    def find_tourist_places_by_distance(
        latitude: float,
        longitude: float,
        max_distance_km: float,
    ) -> dict:
        """
        Find tourist places within a specified distance from a location.

        Args:
            latitude: Latitud del punto de referencia en grados decimales (ej: -25.2822 para Asunción).
            longitude: Longitud del punto de referencia en grados decimales (ej: -57.6352 para Asunción).
            max_distance_km: Distancia máxima en kilómetros desde el punto de referencia (ej: 50.0 para 50 km).

        Returns:
            Dictionary containing total count, formatted table with distances, and raw data.
            Los lugares están ordenados por distancia (más cercanos primero).
        """
        # Get all places
        all_places = place_repository.get_all()

        # Filter places by distance
        places_with_distances = location_service.filter_places_by_distance(
            all_places, latitude, longitude, max_distance_km
        )

        # Format results
        return place_formatter.format_with_distances(places_with_distances)

    @mcp.tool(
        name="get_current_location",
        description="Obtiene la ubicación actual aproximada basada en la dirección IP. Útil para saber dónde estás ubicado antes de buscar lugares cercanos.",
    )
    def get_current_location() -> dict:
        """
        Get current approximate location based on IP address.

        Returns:
            Dictionary with location data including latitude, longitude, city, country, etc.
            Use this to get your current location before searching for nearby places.
        """
        return geolocation_service.get_current_location()

    @mcp.tool(
        name="geocode_location",
        description="Convierte un nombre de ciudad, dirección o lugar a coordenadas (latitud y longitud). Útil para obtener coordenadas de una ubicación antes de buscar lugares cercanos.",
    )
    def geocode_location(
        query: str, country_code: str = "py"
    ) -> dict:
        """
        Convert a location name (city, address, etc.) to coordinates using geocoding.

        Args:
            query: Location name (e.g., "Asunción", "Asunción, Paraguay", "Palacio de los López").
            country_code: Optional country code to limit search (default: "py" for Paraguay).

        Returns:
            Dictionary with location data including latitude, longitude, display_name, etc.
        """
        return geolocation_service.geocode_location(query, country_code)

    @mcp.tool(
        name="find_nearby_tourist_places",
        description="Busca lugares turísticos cercanos automáticamente. Obtiene tu ubicación actual por IP y busca lugares dentro de un rango de distancia. Todo en una sola llamada.",
    )
    def find_nearby_tourist_places(max_distance_km: float = 100.0) -> dict:
        """
        Find nearby tourist places automatically using current IP location.

        This tool:
        1. Gets your current approximate location based on IP
        2. Searches for tourist places within the specified distance
        3. Returns results sorted by distance (closest first)

        Args:
            max_distance_km: Maximum distance in kilometers to search (default: 100.0 km).

        Returns:
            Dictionary with:
            - location: Your current location data
            - places: Tourist places found within the distance
            - error: If location could not be determined
        """
        # Get current location
        location_data = geolocation_service.get_current_location()

        if not location_data.get("success"):
            return {
                "success": False,
                "error": location_data.get("error", "No se pudo determinar la ubicación"),
                "suggestion": "Intenta usar 'geocode_location' con el nombre de tu ciudad o 'find_tourist_places_by_distance' con coordenadas manuales.",
            }

        latitude = location_data.get("latitude")
        longitude = location_data.get("longitude")

        if latitude is None or longitude is None:
            return {
                "success": False,
                "error": "No se pudieron obtener coordenadas de la ubicación",
                "location_data": location_data,
            }

        # Get all places
        all_places = place_repository.get_all()

        # Filter places by distance
        places_with_distances = location_service.filter_places_by_distance(
            all_places, latitude, longitude, max_distance_km
        )

        # Format results
        places_result = place_formatter.format_with_distances(places_with_distances)

        return {
            "success": True,
            "location": {
                "latitude": latitude,
                "longitude": longitude,
                "city": location_data.get("city", ""),
                "country": location_data.get("country", ""),
            },
            "places": places_result,
        }

