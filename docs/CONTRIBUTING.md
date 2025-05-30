# Contributing to Naiyou

Thank you for your interest in contributing to Naiyou! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include screenshots if possible
- Include the version of Python you're using
- Include the version of Naiyou you're using

### Suggesting Enhancements

If you have a suggestion for a new feature or enhancement, please:

- Use a clear and descriptive title
- Provide a detailed description of the proposed functionality
- Explain why this enhancement would be useful
- List any similar features in other applications
- Include screenshots if applicable

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/naiyou.git
   cd naiyou
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

## Testing

We use pytest for testing. To run the tests:

```bash
pytest
```

For coverage report:

```bash
pytest --cov=kanji_processor
```

## Code Style

We use:
- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

The pre-commit hooks will run these automatically. You can also run them manually:

```bash
black .
isort .
flake8
mypy .
```

## Documentation

We use Sphinx for documentation. To build the docs:

```bash
cd docs
make html
```

## Release Process

1. Update version in `setup.py`
2. Update `CHANGELOG.md`
3. Create a new release on GitHub
4. Build and upload to PyPI:
   ```bash
   python -m build
   twine upload dist/*
   ```

## Questions?

Feel free to open an issue for any questions you have about contributing. 