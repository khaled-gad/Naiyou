# Contributing to Kanji Deck Generator

Thank you for your interest in contributing to Kanji Deck Generator! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. Create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce the bug
   - Expected behavior
   - Actual behavior
   - System information (OS, Python version, etc.)
   - Any relevant error messages or logs

### Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue with:
   - A clear, descriptive title
   - Detailed description of the feature
   - Use cases and benefits
   - Any relevant examples

### Pull Requests

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kanji-deck-generator.git
   cd kanji-deck-generator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions and classes
- Keep functions small and focused
- Write meaningful commit messages

## Testing

1. Run tests:
   ```bash
   pytest
   ```

2. Run linting:
   ```bash
   flake8
   ```

3. Run type checking:
   ```bash
   mypy .
   ```

## Documentation

- Update README.md for major changes
- Add docstrings for new functions/classes
- Update documentation in docs/ directory
- Keep examples up to date

## Project Structure

```
kanji-deck-generator/
├── kanji_processor/
│   ├── __init__.py
│   ├── cli.py
│   ├── text_parser.py
│   ├── frequency_analyzer.py
│   ├── dictionary_handler.py
│   ├── anki_generator.py
│   └── utils/
├── tests/
├── docs/
├── README.md
├── setup.py
└── requirements.txt
```

## Release Process

1. Update version in setup.py
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Tag the release
5. Build and upload to PyPI

## Questions?

Feel free to:
- Open an issue
- Contact the maintainers
- Join the community discussions

Thank you for contributing! 