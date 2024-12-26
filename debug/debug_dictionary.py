# debug_dictionary.py
from jamdict import Jamdict
from kanji_processor.dictionary_handler import DictionaryHandler



def inspect_word_data(word):
    jam = Jamdict()
    result = jam.lookup(word)
    
    print(f"\n=== {word} ===")
    
    if not result.entries:
        print("No entries found")
        return
        
    entry = result.entries[0]  # Let's look at first entry
    
    # Raw entry data
    print("\nRaw entry:", entry)
    
    # Kana reading
    if entry.kana_forms:
        print("\nKana forms:")
        for kana in entry.kana_forms:
            print(f"- {kana.text}")  # Using .text to get the actual reading
    
    # Senses (meanings and POS)
    if entry.senses:
        print("\nSenses:")
        for i, sense in enumerate(entry.senses, 1):
            print(f"\nSense {i}:")
            print(f"POS: {sense.pos}")  # Part of speech
            print("Meanings:", [g.text for g in sense.gloss])  # Meanings

def test_dictionary_handler():
    handler = DictionaryHandler()
    test_words = ['勉強', '読む', '例えば']
    
    print("\nTesting Dictionary Handler:")
    print("=" * 40)
    
    for word in test_words:
        info = handler.get_word_info(word)
        print(f"\nWord: {word}")
        print(f"Reading: {info['reading']}")
        print(f"Type: {info['type']}")
        print(f"Meaning: {info['meaning']}")
        

# Add to main():

def main():
    # Test with a variety of words
    test_words = ['勉強', '読む', '楽しい','静か']
    
    for word in test_words:
        inspect_word_data(word)
    
    # Interactive testing
    while True:
        word = input("\nEnter word to inspect (or 'q' to quit): ")
        if word.lower() == 'q':
            break
        inspect_word_data(word)

    print("\nTesting Dictionary Handler...")
    test_dictionary_handler()
    
if __name__ == "__main__":
    main()