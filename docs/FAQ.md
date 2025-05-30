# Frequently Asked Questions

## General Questions

### What is Naiyou?
Naiyou (内容) is a tool that helps you learn Japanese kanji by automatically generating Anki flashcards from any Japanese text you provide. It analyzes the text, identifies unique kanji characters, and creates comprehensive flashcards with readings, meanings, and example words.

### How does Naiyou work?
Naiyou works in three main steps:
1. Analyzes your input text to find unique kanji characters
2. Looks up each kanji's readings, meanings, and example words
3. Generates Anki flashcards with all this information

### Is Naiyou free to use?
Yes! Naiyou is open-source software released under the MIT License. You can use it freely for personal or commercial purposes.

## Installation

### What are the system requirements?
- Python 3.6 or higher
- Anki (to use the generated decks)
- Internet connection (for dictionary lookups)

### How do I install Naiyou?
You can install Naiyou using pip:
```bash
pip install naiyou
```

Or install from source:
```bash
git clone https://github.com/yourusername/naiyou.git
cd naiyou
pip install -e .
```

## Usage

### What kind of input text should I use?
You can use any Japanese text, but for best results:
- Use authentic Japanese content
- Include a variety of contexts
- Consider using graded readers
- Make sure the text is in UTF-8 encoding

### How do I generate a deck?
Basic usage:
```bash
naiyou -i input.txt
```

Advanced usage:
```bash
naiyou -i input.txt -o my_deck.apkg -v
```

### Where is the output deck saved?
By default, the deck is saved as `kanji_deck.apkg` in your current directory. You can specify a different location using the `-o` option.

## Troubleshooting

### The tool can't find some kanji readings
This might happen because:
- The kanji is very rare or obsolete
- The dictionary API is temporarily unavailable
- The kanji is a variant form

Try using more common kanji or check your internet connection.

### The generated deck is too large
You can:
- Use shorter input texts
- Focus on specific topics
- Use the `--max-kanji` option to limit the number of kanji
- Create multiple smaller decks

### The tool is running slowly
This could be due to:
- Large input text
- Slow internet connection
- Many dictionary lookups

Try using smaller texts or check your internet connection.

## Contributing

### How can I contribute to Naiyou?
We welcome contributions! You can:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

See our [Contributing Guide](CONTRIBUTING.md) for details.

### Where can I report issues?
You can report issues on our [GitHub repository](https://github.com/yourusername/naiyou/issues).

## Support

### Where can I get help?
- Check this FAQ
- Open an issue on GitHub
- Join our community discussions
- Read the [documentation](index.md)

### Is there a community?
Yes! You can:
- Join our GitHub discussions
- Follow us on social media
- Share your decks with others

## Technical

### How does the dictionary lookup work?
Naiyou uses the Jisho API to look up kanji information. It fetches:
- On'yomi and kun'yomi readings
- Meanings
- Example words
- JLPT level (if available)

### Can I customize the card format?
Yes! You can:
- Modify the card template in Anki
- Add your own notes
- Create custom fields
- Use different card types

### Is my data private?
Yes! Naiyou:
- Processes all text locally
- Only makes API calls for dictionary lookups
- Doesn't store or share your data
- Doesn't require any login

## Future Development

### What features are planned?
We're working on:
- More dictionary sources
- Custom card templates
- Batch processing
- GUI interface
- Mobile support

### How can I stay updated?
- Watch our GitHub repository
- Follow our releases
- Join our community
- Check our [changelog](CHANGELOG.md) 