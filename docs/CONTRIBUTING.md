# 🤝 Contributing

Contributions are welcome! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/paraguay-tourism-MCP-Server.git
   cd paraguay-tourism-MCP-Server
   ```

3. **Create a virtual environment**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation as needed

3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Provide a clear description of your changes
   - Reference any related issues

## Code Style

- Follow PEP 8 Python style guide
- Use type hints where appropriate
- Write clear, descriptive variable and function names
- Add docstrings to functions and classes

## Architecture Guidelines

When adding new features:

- **Follow SOLID principles**
- **Use dependency injection** via `DependencyContainer`
- **Separate concerns**: handlers → services → repositories
- **Add new handlers** in `handlers/` directory
- **Add new services** in `services/` directory
- **Update documentation** in `docs/` directory

## Testing

Before submitting a PR:

- Test your changes locally
- Ensure the server starts without errors
- Verify MCP tools work correctly

## Documentation

- Update `CHANGELOG.md` for significant changes
- Add or update relevant docs in `docs/`
- Keep README.md concise (move details to docs/)

## Questions?

Feel free to open an issue for questions or discussions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

