# Frequently Asked Questions

## General Questions

### What is Kanji Deck Generator?
Kanji Deck Generator is a tool that automatically creates Anki flashcards from Japanese text. It extracts kanji, finds their readings and meanings, and generates study cards with example words.

### Why should I use this tool?
- Learn kanji in context with real example words
- Save time by automating flashcard creation
- Study kanji that appear in texts you're actually reading
- Get comprehensive information including readings and meanings

### Do I need to know Japanese to use this tool?
No, but you'll need:
- Some Japanese text to input
- Anki installed on your computer
- Basic command-line knowledge

## Technical Questions

### What are the system requirements?
- Python 3.6 or higher
- Anki (to use the generated decks)
- Internet connection (for dictionary lookups)

### How do I install the tool?
```bash
pip install kanji-deck-generator
```
Or from source:
```bash
git clone https://github.com/yourusername/kanji-deck-generator.git
cd kanji-deck-generator
pip install -e .
```

### Why do I need an internet connection?
The tool uses online dictionaries to look up kanji readings and meanings. This ensures you get accurate and up-to-date information.

## Usage Questions

### What kind of input text should I use?
- Any Japanese text in UTF-8 encoding
- Text files (.txt)
- Authentic Japanese content (articles, stories, etc.)
- Graded readers for beginners

### How do I generate a deck?
```bash
generate-kanji-deck -i input.txt
```

### Can I customize the output deck?
Yes, you can:
- Change the output filename with `-o` option
- Get detailed processing info with `-v` option
- Modify the cards in Anki after importing

### What information is included in each card?
- Kanji character
- On'yomi and kun'yomi readings
- Meaning
- Example words with readings and meanings

## Troubleshooting

### The tool can't find some kanji readings
This might happen because:
- The kanji is rare or obsolete
- The dictionary doesn't have the entry
- The internet connection is unstable

Try:
- Using more common kanji
- Checking your internet connection
- Using a different text source

### The generated deck is too large
To manage deck size:
- Use shorter input texts
- Focus on specific topics
- Create multiple smaller decks
- Use Anki's filtering features

### Some words are missing readings
This can happen with:
- Rare words
- Proper nouns
- New words not in the dictionary
- Conjugated forms

Try:
- Using the base form of words
- Adding your own readings in Anki
- Using more common vocabulary

## Advanced Usage

### Can I use this with other SRS systems?
Currently, the tool only generates Anki decks (.apkg files). However, you can:
- Export from Anki to other formats
- Use Anki's export features
- Convert the deck to other formats

### How can I contribute to the project?
You can:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation
- Share your use cases

### Is there a way to batch process multiple files?
Currently, the tool processes one file at a time. You can:
- Use shell scripts to process multiple files
- Combine files before processing
- Create separate decks for different texts

## Support

### Where can I get help?
- GitHub Issues
- Documentation
- Community discussions
- Email support

### How do I report a bug?
1. Check if it's already reported
2. Create a new issue on GitHub
3. Include:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - System information

### Can I request new features?
Yes! Please:
- Check existing issues first
- Create a new issue
- Describe the feature
- Explain its benefits
- Provide examples if possible 