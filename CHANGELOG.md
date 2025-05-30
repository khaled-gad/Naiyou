# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive documentation in the `docs/` directory
- GitHub Pages site for better documentation accessibility
- Contributing guidelines
- Code of Conduct
- FAQ section
- Development setup instructions
- Pre-commit hooks for code quality
- Type hints throughout the codebase
- Test coverage reporting

### Changed
- Rebranded project from "Kanji Deck Generator" to "Naiyou (内容)"
- Updated command-line interface from `generate-kanji-deck` to `naiyou`
- Improved error handling and user feedback
- Enhanced dictionary lookup reliability
- Optimized card generation process

### Fixed
- Dictionary lookup failures for rare kanji
- Memory usage during large text processing
- Card template formatting issues
- Encoding problems with non-UTF-8 input files

## [0.1.0] - 2024-03-20

### Added
- Initial release
- Basic kanji extraction from text
- Dictionary lookup functionality
- Anki deck generation
- Command-line interface
- Support for UTF-8 text files
- Basic error handling
- Simple progress reporting

### Dependencies
- fugashi for Japanese text tokenization
- unidic-lite for Japanese dictionary
- jamdict for Japanese dictionary data
- genanki for Anki deck generation
- requests for HTTP requests 