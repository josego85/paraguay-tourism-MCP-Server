# Usage Guide: Distance Search and Geolocation

## 🎯 Get Your Current Location

### Option 1: `get_current_location` (Recommended for Cursor Desktop)

**Automatically gets your location based on your IP address.**

```python
# In Cursor Desktop, simply ask:
# "Where am I located?"

# Or use directly:
location = get_current_location()
# Returns: {"success": True, "latitude": -25.2822, "longitude": -57.6352, "city": "Asunción", ...}
```

**Advantages:**
- ✅ Automatic, you don't need to know your coordinates
- ✅ Works in Cursor Desktop
- ✅ No special permissions required

**Limitations:**
- ⚠️ Approximate precision (based on IP, not GPS)
- ⚠️ May show your internet provider's location, not your exact location

### Option 2: `geocode_location`

**Converts a city name or address to coordinates.**

```python
# Example: Get coordinates of a city
coords = geocode_location("Asunción, Paraguay")
# Returns: {"success": True, "latitude": -25.2822, "longitude": -57.6352, ...}

# Also works with specific addresses
coords = geocode_location("Palacio de los López, Asunción")
```

### Option 3: `find_nearby_tourist_places` (All-in-One)

**Gets your location AND searches for nearby places automatically.**

```python
# Search for places within 100 km automatically
result = find_nearby_tourist_places(max_distance_km=100.0)

# Returns:
# {
#   "success": True,
#   "location": {"latitude": ..., "longitude": ..., "city": ...},
#   "places": { ... found places ... }
# }
```

## 🔍 Manual Search: `find_tourist_places_by_distance`

This tool allows you to search for tourist places within a distance range from a specific location (when you already know the coordinates).

### Parameters

- `latitude` (float): Latitude of the reference point in decimal degrees
- `longitude` (float): Longitude of the reference point in decimal degrees  
- `max_distance_km` (float): Maximum distance in kilometers from the reference point

### Usage Example

```python
# Search for places within 100 km from Asunción
result = find_tourist_places_by_distance(
    latitude=-25.2822,      # Asunción
    longitude=-57.6352,     # Asunción
    max_distance_km=100.0
)
```

## 📍 How to Get Coordinates (Manual Alternatives)

If automatic tools don't work, you can get coordinates manually:

### Option 1: Google Maps
1. Open [Google Maps](https://www.google.com/maps)
2. Search for the location or click on the map
3. Right-click on the point and select coordinates
4. Coordinates will appear in decimal format (e.g., -25.2822, -57.6352)

### Option 2: Known City Coordinates

**Main Cities of Paraguay:**
- **Asunción**: lat=-25.2822, lng=-57.6352
- **Ciudad del Este**: lat=-25.5097, lng=-54.6117
- **Encarnación**: lat=-27.3306, lng=-55.8667
- **Pedro Juan Caballero**: lat=-22.6503, lng=-56.0139

## Result

The tool returns:
- `total`: Number of places found
- `table`: Formatted table with places and distances
- `raw`: List of places with complete data including `distance_km`

Places are **sorted by distance** (closest first).

## 💡 Recommended Workflow in Cursor Desktop

### Scenario 1: "I want to know where I am and what places are nearby"

```python
# Step 1: Get your location
location = get_current_location()

# Step 2: If you have coordinates, search for nearby places
if location.get("success"):
    places = find_tourist_places_by_distance(
        latitude=location["latitude"],
        longitude=location["longitude"],
        max_distance_km=50.0
    )
```

### Scenario 2: "Search for places near a specific city"

```python
# Step 1: Get coordinates of the city
coords = geocode_location("Encarnación, Paraguay")

# Step 2: Search for nearby places
if coords.get("success"):
    places = find_tourist_places_by_distance(
        latitude=coords["latitude"],
        longitude=coords["longitude"],
        max_distance_km=100.0
    )
```

### Scenario 3: "All-in-one" (Simplest)

```python
# A single call that does everything automatically
result = find_nearby_tourist_places(max_distance_km=100.0)
```

## 🔧 Technical Notes

- **Haversine Formula**: Used to calculate distances on the Earth's surface
- **Precision**: ~0.5% error for typical distances
- **Earth Radius**: 6,371 km
- **IP Geolocation**: Approximate precision (city/regional level)
- **Geocoding**: Uses OpenStreetMap Nominatim (free, no API key required)
- **Dependency**: `httpx` for HTTP requests (already included in requirements.txt)
