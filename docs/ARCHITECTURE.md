# 🏗️ Architecture

This project follows **senior developer best practices** with a clean, modular architecture based on SOLID principles.

## Architecture Overview

```
┌─────────────────┐
│   MCP Server    │
└────────┬────────┘
         │
    ┌────┴────┐
    │ Handlers│  ← MCP Tools Registration
    └────┬────┘
         │
    ┌────┴────┐
    │ Services │  ← Business Logic Layer
    └────┬────┘
         │
    ┌────┴────┐
    │Repository│  ← Data Access Layer
    └────┬────┘
         │
    ┌────┴────┐
    │  Models │  ← Data Models
    └─────────┘
```

## Project Structure

```
paraguay-tourism-MCP-Server/
├── src/
│   └── paraguay_tourism/
│       ├── core/              # Dependency injection & configuration
│       │   ├── dependencies.py
│       │   └── imports.py
│       ├── handlers/          # MCP tool handlers
│       │   └── place_handlers.py
│       ├── models/           # Data models
│       │   └── place.py
│       ├── repositories/       # Data access layer
│       │   └── place_repository.py
│       ├── services/           # Business logic
│       │   ├── geolocation_service.py
│       │   ├── location_service.py
│       │   └── place_formatter.py
│       └── server.py          # MCP server entry point
├── data/
│   ├── places.json            # Paraguay tourist places
│   └── places_germany.json    # Test data (Germany)
├── docs/                       # Documentation
└── requirements.txt            # Python dependencies
```

## Key Components

### `core/`
Dependency injection container and configuration management.

- **`dependencies.py`**: `DependencyContainer` class managing all service instances
- **`imports.py`**: Handles relative/absolute import configuration

### `handlers/`
MCP tool handlers that register and implement MCP tools.

- **`place_handlers.py`**: All place-related MCP tools registration

### `services/`
Business logic layer containing reusable services.

- **`location_service.py`**: Distance calculations using Haversine formula
- **`geolocation_service.py`**: IP geolocation and geocoding services
- **`place_formatter.py`**: Data formatting for output

### `repositories/`
Data access layer abstracting data source.

- **`place_repository.py`**: Place data access methods

### `models/`
Pydantic data models with validation.

- **`place.py`**: Place model definition

## Design Principles

### SOLID Principles

- **Single Responsibility**: Each module has one clear purpose
- **Open/Closed**: Easy to extend without modifying existing code
- **Liskov Substitution**: Interfaces are properly abstracted
- **Interface Segregation**: Focused, specific interfaces
- **Dependency Inversion**: Dependencies injected via container

### Benefits

- ✅ **Testability**: Easy to mock dependencies for unit testing
- ✅ **Maintainability**: Clear separation of concerns
- ✅ **Extensibility**: Simple to add new features
- ✅ **Scalability**: Architecture supports growth

## Data Flow

1. **MCP Request** → Server receives tool call
2. **Handler** → Routes to appropriate handler function
3. **Service** → Business logic processing
4. **Repository** → Data access
5. **Model** → Data validation and transformation
6. **Formatter** → Output formatting
7. **Response** → Returns formatted result to MCP client

## Technologies

- **FastMCP**: MCP server framework
- **Pydantic**: Data validation
- **httpx**: HTTP client for external APIs
- **tabulate**: Table formatting

