# kanji_processor/cli.py
import argparse
import sys
from pathlib import Path
from .text_parser import JapaneseTextParser
from .frequency_analyzer import FrequencyAnalyzer
from .anki_generator import AnkiDeckGenerator
from .dictionary_handler import DictionaryHandler

def read_input_text(filename):
    """Read Japanese text from input file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def process_text(text, dict_handler, analyzer, verbose=False):
    """Process text and return kanji data."""
    if verbose:
        print("Analyzing text...")
    
    # Get frequency analysis
    kanji_freq = analyzer.get_sorted_kanji(text)
    word_freq = analyzer.get_sorted_words(text)
    word_freq_dict = dict(word_freq)
    
    if verbose:
        print(f"\nFound {len(kanji_freq)} unique kanji")
        print(f"Found {len(word_freq)} unique words")
    
    # Prepare data for Anki deck
    kanji_data = []
    processed_words = set()
    
    for kanji, freq in kanji_freq:
        if verbose:
            print(f"\nProcessing kanji: {kanji}")
        
        kanji_words = []
        for word, freq in word_freq:
            if kanji in word and word not in processed_words:
                # Handle word conjugations
                lookup_word = word
                if word.endswith(('っ', 'ん', 'い')):
                    lookup_word = word[:-1]
                elif word.endswith('います'):
                    lookup_word = word[:-3]
                elif word.endswith('ます'):
                    lookup_word = word[:-2]
                
                try:
                    word_info = dict_handler.get_word_info(lookup_word)
                    if word_info['reading'] or word_info['meaning']:
                        kanji_words.append((word, word_info))
                        processed_words.add(word)
                        if verbose:
                            print(f"  Added word: {word}")
                except Exception as e:
                    if verbose:
                        print(f"  Error processing word {word}: {str(e)}")
                    continue
        
        if kanji_words:
            # Get kanji readings
            readings = dict_handler.get_kanji_readings(kanji)
            
            kanji_data.append({
                'kanji': kanji,
                'on_yomi': readings['on_yomi'],
                'kun_yomi': readings['kun_yomi'],
                'common_words': sorted(kanji_words, 
                                     key=lambda x: word_freq_dict.get(x[0], 0),
                                     reverse=True)
            })
    
    return kanji_data

def main():
    """Main entry point for the command line interface."""
    parser = argparse.ArgumentParser(
        description='Generate Anki cards from Japanese text.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  generate-kanji-deck -i input.txt
  generate-kanji-deck -i input.txt -o my_deck.apkg
  generate-kanji-deck -i input.txt -v
        """
    )
    
    parser.add_argument('-i', '--input', 
                       required=True,
                       help='Input text file path')
    parser.add_argument('-o', '--output',
                       help='Output Anki deck file path (default: kanji_deck.apkg)')
    parser.add_argument('-v', '--verbose',
                       action='store_true',
                       help='Show detailed processing information')
    
    args = parser.parse_args()
    
    # Set output filename
    output_file = args.output or 'kanji_deck.apkg'
    
    # Read input text
    if args.verbose:
        print(f"Reading input file: {args.input}")
    
    text = read_input_text(args.input)
    if not text:
        sys.exit(1)
    
    try:
        # Initialize components
        analyzer = FrequencyAnalyzer()
        dict_handler = DictionaryHandler()
        
        # Process text
        kanji_data = process_text(text, dict_handler, analyzer, args.verbose)
        
        # Generate Anki deck
        if kanji_data:
            if args.verbose:
                print("\nGenerating Anki deck...")
            
            deck_generator = AnkiDeckGenerator()
            deck = deck_generator.generate_deck(kanji_data, "Kanji from Text")
            deck_generator.save_deck(deck, output_file)
            
            # Print summary
            print("\nDeck Generation Summary:")
            print("-" * 40)
            print(f"Total unique kanji processed: {len(kanji_data)}")
            total_words = sum(len(k['common_words']) for k in kanji_data)
            print(f"Total word examples included: {total_words}")
            print(f"\nDeck generated: {output_file}")
            
            if args.verbose:
                print("\nSample card data:")
                sample = kanji_data[0]
                print(f"Kanji: {sample['kanji']}")
                print(f"On'yomi: {sample['on_yomi']}")
                print(f"Kun'yomi: {sample['kun_yomi']}")
                print("Common words:")
                for word, info in sample['common_words'][:3]:
                    print(f"  - {word} ({info['reading']}) {info['type']} : {info['meaning']}")
        else:
            print("\nNo valid kanji data found to generate deck")
            
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError during processing: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()