# 🚀 Paraguay Tourism MCP Server

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/paraguay-tourism-MCP-Server)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange.svg)](https://modelcontextprotocol.io/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.13.0-purple.svg)](https://github.com/jlowin/fastmcp)

> A Model Context Protocol (MCP) server providing access to Paraguay's tourist places with advanced location-based search capabilities.

## ✨ Features

- 🗺️ Complete tourist places database
- 📍 Location-based search with distance calculations
- 🌐 Automatic IP-based geolocation
- 🔍 Geocoding support (city/address to coordinates)
- 🎯 Results sorted by distance
- 🏗️ Clean architecture following SOLID principles

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/paraguay-tourism-MCP-Server.git
cd paraguay-tourism-MCP-Server

# Setup virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python src/paraguay_tourism/server.py
```

## 📚 Documentation

- 📖 **[Installation Guide](docs/INSTALLATION.md)** - Setup and configuration
- 🏗️ **[Architecture](docs/ARCHITECTURE.md)** - Project structure and design
- 🛠️ **[API Reference](docs/API.md)** - Complete MCP tools documentation
- 📍 **[Location Usage](docs/LOCATION_USAGE.md)** - Location-based features guide
- 🤝 **[Contributing](docs/CONTRIBUTING.md)** - Contribution guidelines
- 📝 **[CHANGELOG](CHANGELOG.md)** - Version history

## 🛠️ MCP Tools

| Tool | Description |
|------|-------------|
| `list_all_tourist_places` | List all tourist places |
| `get_tourist_place_by_id` | Get place details by ID |
| `find_tourist_places_by_distance` | Search by distance from coordinates |
| `get_current_location` | Get location via IP |
| `geocode_location` | Convert address to coordinates |
| `find_nearby_tourist_places` | Auto-location + nearby search |

See [API Reference](docs/API.md) for complete documentation.

## 🔧 Technologies

- **Python 3.11+**
- **FastMCP** - MCP server framework
- **Pydantic** - Data validation
- **httpx** - HTTP client
- **tabulate** - Table formatting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [OpenStreetMap Nominatim](https://nominatim.openstreetmap.org/)
- [ip-api.com](http://ip-api.com/)

---

<div align="center">

**Made with ❤️ for Paraguay Tourism**

[⭐ Star](https://github.com/yourusername/paraguay-tourism-MCP-Server) | [🐛 Report Bug](https://github.com/yourusername/paraguay-tourism-MCP-Server/issues) | [💡 Request Feature](https://github.com/yourusername/paraguay-tourism-MCP-Server/issues)

</div>
