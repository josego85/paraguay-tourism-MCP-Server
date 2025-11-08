# 🛠️ API Reference

Complete reference for all MCP tools provided by the server.

## Available Tools

| Tool | Description |
|------|-------------|
| `list_all_tourist_places` | List all tourist places in Paraguay |
| `get_tourist_place_by_id` | Get detailed information about a specific place |
| `find_tourist_places_by_distance` | Search places within a distance from coordinates |
| `get_current_location` | Get your current location via IP geolocation |
| `geocode_location` | Convert city/address names to coordinates |
| `find_nearby_tourist_places` | All-in-one: get location and search nearby places |

## Tool Details

### `list_all_tourist_places`

Lists all tourist places in Paraguay with name, city, category, and GPS coordinates.

**Parameters:** None

**Returns:**
```json
{
  "total": 8,
  "table": "Formatted table string",
  "raw": [
    {
      "id": "palacio-lopez",
      "name": "Palacio de los López",
      "description": "...",
      "category": "Arquitectura",
      "lat": -25.2822,
      "lng": -57.6352,
      "city": "Asunción",
      "region": "Capital"
    }
  ]
}
```

### `get_tourist_place_by_id`

Retrieves detailed information about a specific tourist place by ID.

**Parameters:**
- `place_id` (string): The ID of the place to retrieve

**Returns:**
```json
{
  "found": true,
  "place": {
    "id": "palacio-lopez",
    "name": "Palacio de los López",
    "description": "...",
    "category": "Arquitectura",
    "lat": -25.2822,
    "lng": -57.6352,
    "city": "Asunción",
    "region": "Capital"
  }
}
```

**Error Response:**
```json
{
  "found": false,
  "message": "Lugar turístico no encontrado"
}
```

### `find_tourist_places_by_distance`

Searches for tourist places within a specified distance from given coordinates.

**Parameters:**
- `latitude` (float): Latitude of the reference point in decimal degrees
- `longitude` (float): Longitude of the reference point in decimal degrees
- `max_distance_km` (float): Maximum distance in kilometers from the reference point

**Returns:**
```json
{
  "total": 3,
  "table": "Formatted table with distances",
  "raw": [
    {
      "id": "palacio-lopez",
      "name": "Palacio de los López",
      "distance_km": 0.5,
      ...
    }
  ]
}
```

**Note:** Results are sorted by distance (closest first).

### `get_current_location`

Automatically detects user's approximate location based on IP address.

**Parameters:** None

**Returns:**
```json
{
  "success": true,
  "latitude": 50.1169,
  "longitude": 8.6837,
  "city": "Frankfurt am Main",
  "country": "Germany",
  "country_code": "DE",
  "ip": "159.26.104.7"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message"
}
```

### `geocode_location`

Converts location names (cities, addresses) to GPS coordinates.

**Parameters:**
- `query` (string): Location name (e.g., "Asunción, Paraguay")
- `country_code` (string, optional): Country code to limit search (default: "py")

**Returns:**
```json
{
  "success": true,
  "latitude": -25.2822,
  "longitude": -57.6352,
  "display_name": "Asunción, Paraguay",
  "query": "Asunción, Paraguay"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "No se encontró la ubicación: Asunción"
}
```

### `find_nearby_tourist_places`

All-in-one tool that automatically gets user location and searches for nearby places.

**Parameters:**
- `max_distance_km` (float, optional): Maximum distance in kilometers (default: 100.0)

**Returns:**
```json
{
  "success": true,
  "location": {
    "latitude": 50.1169,
    "longitude": 8.6837,
    "city": "Frankfurt am Main",
    "country": "Germany"
  },
  "places": {
    "total": 5,
    "table": "...",
    "raw": [...]
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "No se pudo determinar la ubicación",
  "suggestion": "Intenta usar 'geocode_location' con el nombre de tu ciudad..."
}
```

## Usage Examples

### Get Current Location

```python
location = get_current_location()
if location.get("success"):
    print(f"Location: {location['city']}, {location['country']}")
```

### Search Nearby Places

```python
places = find_tourist_places_by_distance(
    latitude=-25.2822,
    longitude=-57.6352,
    max_distance_km=50.0
)
print(f"Found {places['total']} places")
```

### Geocode a City

```python
coords = geocode_location("Asunción, Paraguay")
if coords.get("success"):
    print(f"Coordinates: {coords['latitude']}, {coords['longitude']}")
```

### All-in-One Search

```python
result = find_nearby_tourist_places(max_distance_km=100.0)
if result.get("success"):
    print(f"Found {result['places']['total']} places near {result['location']['city']}")
```

## See Also

- [Location Usage Guide](LOCATION_USAGE.md) - Detailed guide for location-based features
- [Installation Guide](INSTALLATION.md) - Setup instructions

