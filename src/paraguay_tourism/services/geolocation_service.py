"""Service for geolocation operations (IP-based and geocoding)."""

import json
from typing import Dict, Optional, Tuple

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False


class GeolocationService:
    """Service for obtaining user location via IP or geocoding."""

    # Free IP geolocation service (no API key required)
    IP_API_URL = "http://ip-api.com/json/"
    
    # Free geocoding service (OpenStreetMap Nominatim)
    GEOCODING_URL = "https://nominatim.openstreetmap.org/search"

    @staticmethod
    def get_location_by_ip(ip: Optional[str] = None) -> Dict:
        """
        Get approximate location based on IP address.

        Args:
            ip: IP address to geolocate. If None, uses the current public IP.

        Returns:
            Dictionary with location data including latitude, longitude, city, country, etc.
            Returns error dict if geolocation fails.
        """
        if not HTTPX_AVAILABLE:
            return {
                "success": False,
                "error": "httpx library not available. Install it with: pip install httpx",
            }

        try:
            url = GeolocationService.IP_API_URL
            if ip:
                url += ip
            else:
                url += "?fields=status,message,lat,lon,city,country,countryCode,query"

            with httpx.Client(timeout=5.0) as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()

            if data.get("status") == "fail":
                return {
                    "success": False,
                    "error": data.get("message", "Geolocation failed"),
                }

            return {
                "success": True,
                "latitude": data.get("lat"),
                "longitude": data.get("lon"),
                "city": data.get("city", ""),
                "country": data.get("country", ""),
                "country_code": data.get("countryCode", ""),
                "ip": data.get("query", ip),
                "raw": data,
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error getting location by IP: {str(e)}",
            }

    @staticmethod
    def geocode_location(
        query: str, country_code: Optional[str] = "py"
    ) -> Dict:
        """
        Convert a location name (city, address, etc.) to coordinates using geocoding.

        Args:
            query: Location name (e.g., "Asunción", "Asunción, Paraguay", "Palacio de los López").
            country_code: Optional country code to limit search (default: "py" for Paraguay).

        Returns:
            Dictionary with location data including latitude, longitude, display_name, etc.
            Returns error dict if geocoding fails.
        """
        if not HTTPX_AVAILABLE:
            return {
                "success": False,
                "error": "httpx library not available. Install it with: pip install httpx",
            }

        try:
            params = {
                "q": query,
                "format": "json",
                "limit": 1,
                "addressdetails": 1,
            }
            
            if country_code:
                params["countrycodes"] = country_code

            headers = {
                "User-Agent": "Paraguay-Tourism-MCP-Server/1.0 (contact: tourism@example.com)",
            }

            with httpx.Client(timeout=10.0, headers=headers) as client:
                response = client.get(GeolocationService.GEOCODING_URL, params=params)
                response.raise_for_status()
                results = response.json()

            if not results:
                return {
                    "success": False,
                    "error": f"No se encontró la ubicación: {query}",
                }

            result = results[0]
            return {
                "success": True,
                "latitude": float(result.get("lat", 0)),
                "longitude": float(result.get("lon", 0)),
                "display_name": result.get("display_name", ""),
                "query": query,
                "raw": result,
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error en geocoding: {str(e)}",
            }

    @staticmethod
    def get_current_location() -> Dict:
        """
        Get current location using IP geolocation (convenience method).

        Returns:
            Dictionary with location data or error.
        """
        return GeolocationService.get_location_by_ip()

