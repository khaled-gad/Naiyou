# Kanji Deck Generator Documentation

Welcome to the Kanji Deck Generator documentation! This tool helps you learn Japanese kanji by automatically generating Anki flashcards from any Japanese text you provide.

## Quick Start

1. **Install the tool**:
   ```bash
   pip install kanji-deck-generator
   ```

2. **Create a text file** with Japanese content (e.g., `input.txt`)

3. **Generate your deck**:
   ```bash
   generate-kanji-deck -i input.txt
   ```

4. **Import the deck** into Anki

## Detailed Guide

### Installation

#### Prerequisites
- Python 3.6 or higher
- Anki (to use the generated decks)

#### Installation Methods

1. **Using pip**:
   ```bash
   pip install kanji-deck-generator
   ```

2. **From source**:
   ```bash
   git clone https://github.com/yourusername/kanji-deck-generator.git
   cd kanji-deck-generator
   pip install -e .
   ```

### Usage

#### Basic Usage
The simplest way to use the tool is:
```bash
generate-kanji-deck -i input.txt
```
This will create a deck named `kanji_deck.apkg` in the current directory.

#### Advanced Usage
For more control, you can use additional options:
```bash
generate-kanji-deck -i input.txt -o my_deck.apkg -v
```

#### Command Line Options

| Option | Description |
|--------|-------------|
| `-i, --input` | Input text file path (required) |
| `-o, --output` | Output Anki deck file path (default: kanji_deck.apkg) |
| `-v, --verbose` | Show detailed processing information |

### How It Works

1. **Text Analysis**
   - The tool reads your Japanese text
   - Identifies unique kanji characters
   - Analyzes word frequency

2. **Dictionary Lookup**
   - Looks up readings (on'yomi and kun'yomi)
   - Finds meanings
   - Identifies example words

3. **Card Generation**
   - Creates flashcards for each kanji
   - Includes readings and meanings
   - Adds example words with context

### Example

Let's say you have this text:
```
私は日本語を勉強しています。
```

The tool will:
1. Extract kanji: 私, 日, 本, 語, 勉, 強
2. For each kanji, it will:
   - Find readings (e.g., 私: シ, わたくし)
   - Look up meanings
   - Find example words
3. Generate cards like:

Front:
```
私
```

Back:
```
Readings:
- On'yomi: シ
- Kun'yomi: わたくし

Meaning: I, private

Example words:
- 私 (わたし) - I, me
- 私立 (しりつ) - private (institution)
```

### Tips for Best Results

1. **Input Text Quality**
   - Use authentic Japanese text
   - Include a variety of contexts
   - Consider using graded readers

2. **Deck Management**
   - Review cards regularly in Anki
   - Use the example words to learn kanji in context
   - Focus on high-frequency kanji first

3. **Customization**
   - You can modify the card template in Anki
   - Add your own notes or mnemonics
   - Create subdecks for different topics

### Troubleshooting

Common issues and solutions:

1. **Dictionary Lookup Fails**
   - Ensure you have internet connection
   - Check if the word exists in the dictionary
   - Try using the base form of conjugated words

2. **Card Generation Issues**
   - Verify your input text is in UTF-8 encoding
   - Check if the text contains valid Japanese characters
   - Ensure you have write permissions in the output directory

### Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Support

If you need help:
- Open an issue on GitHub
- Check the [FAQ](FAQ.md)
- Join our community discussions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 