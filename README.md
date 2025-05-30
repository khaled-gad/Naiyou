# Naiyou (内容)

A powerful tool that automatically generates Anki flashcards from Japanese text, helping you learn kanji in context.

## Features

- Extract kanji from any Japanese text
- Generate Anki flashcards with:
  - Kanji readings (on'yomi and kun'yomi)
  - Example words containing the kanji
  - Word meanings and readings
- Frequency analysis of kanji and words
- Support for word conjugations
- Command-line interface for easy use

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/naiyou.git
cd naiyou
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

Basic usage:
```bash
naiyou -i input.txt
```

Advanced usage:
```bash
naiyou -i input.txt -o my_deck.apkg -v
```

### Command Line Arguments

- `-i, --input`: Input text file path (required)
- `-o, --output`: Output Anki deck file path (default: kanji_deck.apkg)
- `-v, --verbose`: Show detailed processing information

## How It Works

1. The tool reads your Japanese text input
2. Analyzes the text to find unique kanji and their frequency
3. Looks up each kanji's readings and meanings using a dictionary
4. Finds example words containing each kanji
5. Generates Anki flashcards with all this information
6. Creates an Anki deck file (.apkg) that you can import into Anki

## Example

Input text:
```
私は日本語を勉強しています。
```

The tool will:
1. Extract kanji: 私, 日, 本, 語, 勉, 強
2. Look up readings and meanings
3. Find example words
4. Generate flashcards with:
   - Kanji on front
   - Readings and meanings on back
   - Example words with readings and meanings

## Requirements

- Python 3.6+
- Anki (to use the generated decks)

## Dependencies

- fugashi: Japanese text tokenization
- unidic-lite: Japanese dictionary
- jamdict: Japanese dictionary data
- genanki: Anki deck generation
- requests: HTTP requests

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Uses the JAMDict project for Japanese dictionary data
