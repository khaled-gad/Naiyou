# test.py
import argparse
import sys
import os
import textwrap
from kanji_processor.text_parser import JapaneseTextParser
from kanji_processor.frequency_analyzer import FrequencyAnalyzer
from kanji_processor.anki_generator import AnkiDeckGenerator
from kanji_processor.dictionary_handler import DictionaryHandler

def read_input_text(filename="input_text.txt"):
    """Read and return the content of the input file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def test_basic_functionality(input_file="input_text.txt", output_file="kanji_study.apkg"):
    """Main function to process text and generate Anki deck."""
    # Read input text
    text = read_input_text(input_file)
    if not text:
        print("No input text to process.")
        return
    
    print(f"\nProcessing text from: {input_file}")
    print("-" * 40)
    
    try:
        # Initialize components
        analyzer = FrequencyAnalyzer()
        dict_handler = DictionaryHandler()
        
        # Get frequency analysis
        print("Analyzing text frequencies...")
        kanji_freq = analyzer.get_sorted_kanji(text)
        word_freq = analyzer.get_sorted_words(text)
        
        if not isinstance(kanji_freq, list):
            print("Error: Unexpected frequency analyzer output")
            return
        
        # Print analysis results
        print("\nKanji Frequency:")
        for kanji, freq in kanji_freq:
            print(f"{kanji}: {freq}")
        
        print("\nWord Frequency:")
        for word, freq in word_freq:
            print(f"{word}: {freq}")
        
        # Prepare data for Anki deck
        print("\nPreparing Anki deck data...")
        kanji_data = []
        processed_words = set()
        
        # Convert word_freq to dictionary
        word_freq_dict = dict(word_freq)
        
        for kanji, kanji_freq_count in kanji_freq:
            kanji_words = []
            
            # Iterate over the word frequency dictionary items
            for word, freq in word_freq_dict.items():
                if kanji in word and word not in processed_words:
                    # Remove conjugation endings for better dictionary lookup
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
                            kanji_words.append((word, {
                                'reading': word_info['reading'],
                                'type': word_info['type'],
                                'meaning': word_info['meaning']
                            }))
                            processed_words.add(word)
                    except Exception as e:
                        print(f"Error processing word {word}: {str(e)}")
                        continue
            
            if kanji_words:
                kanji_data.append({
                    'kanji': kanji,
                    'on_yomi': 'オン',
                    'kun_yomi': 'くん',
                    'common_words': sorted(kanji_words, 
                                         key=lambda x: word_freq_dict.get(x[0], 0),
                                         reverse=True)
                })
        
        # Generate Anki deck
        if kanji_data:
            print("\nGenerating Anki deck...")
            deck_generator = AnkiDeckGenerator()
            deck = deck_generator.generate_deck(kanji_data, "Kanji from Text")
            deck_generator.save_deck(deck, output_file)
            
            # Print summary
            print("\nDeck Generation Summary:")
            print("-" * 40)
            print(f"Total unique kanji processed: {len(kanji_data)}")
            print(f"Kanji cards created: {len(kanji_data)}")
            total_words = sum(len(k['common_words']) for k in kanji_data)
            print(f"Total word examples included: {total_words}")
            print(f"\nAnki deck generated: {output_file}")
            
            # Print sample card data
            if kanji_data:
                print("\nSample card data:")
                print("-" * 40)
                sample = kanji_data[0]
                print(f"Kanji: {sample['kanji']}")
                print(f"On'yomi: {sample['on_yomi']}")
                print(f"Kun'yomi: {sample['kun_yomi']}")
                print("Common words:")
                for word, info in sample['common_words'][:3]:
                    print(f"  - {word} ({info['reading']}) {info['type']} : {info['meaning']}")
        else:
            print("\nNo valid kanji data found to generate deck")
            
    except Exception as e:
        print(f"\nError during processing: {str(e)}")
        raise

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Generate Anki cards from Japanese text.'
    )
    parser.add_argument('-i', '--input', 
                       default='input_text.txt',
                       help='Input text file path (default: input_text.txt)')
    parser.add_argument('-o', '--output',
                       default='kanji_study.apkg',
                       help='Output Anki deck file path (default: kanji_study.apkg)')
    return parser.parse_args()

if __name__ == "__main__":
    try:
        args = parse_arguments()
        test_basic_functionality(args.input, args.output)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError running test: {str(e)}")
        raise