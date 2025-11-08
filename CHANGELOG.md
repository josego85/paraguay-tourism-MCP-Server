# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-08

### Added

- **Architecture refactoring** following SOLID principles
  - Modular structure: `core/`, `handlers/`, `services/`, `repositories/`, `models/`
  - Dependency Injection Container pattern
  - Factory pattern for server initialization

- **Location services**
  - `LocationService`: Haversine formula for distance calculations
  - `GeolocationService`: IP-based geolocation and geocoding (OpenStreetMap Nominatim)
  - Results sorted by distance (closest first)

- **MCP Tools** (6 tools)
  - `list_all_tourist_places`: List all tourist places
  - `get_tourist_place_by_id`: Get place details by ID
  - `find_tourist_places_by_distance`: Search by distance from coordinates
  - `get_current_location`: Get location via IP geolocation
  - `geocode_location`: Convert city/address to coordinates
  - `find_nearby_tourist_places`: Auto-location + nearby search

- **Data layer**
  - `Place` model (Pydantic)
  - `PlaceRepository` for data access
  - `PlaceFormatter` for output formatting

- **Documentation**
  - `README.md`: Professional badges, quick start guide
  - `docs/INSTALLATION.md`: Setup and configuration
  - `docs/ARCHITECTURE.md`: Architecture and design principles
  - `docs/API.md`: Complete API reference
  - `docs/LOCATION_USAGE.md`: Location features guide
  - `docs/CONTRIBUTING.md`: Contribution guidelines

- **Data files**
  - `data/places.json`: 8 tourist places in Paraguay
  - `data/places_germany.json`: Test dataset (12 places near Frankfurt)

### Changed

- **Server structure** (`server.py`): Reduced from 63 to 49 lines, improved separation of concerns
- **README.md**: Simplified from 244 to 88 lines, moved details to separate docs

---

## Version History

- **1.0.0**: Initial release with complete refactoring, location services, and MCP tools
