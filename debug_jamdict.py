# debug_jmdict.py
from jamdict import Jamdict
import json
from pprint import pprint

def entry_to_dict(entry):
    """Convert JMdict entry to dictionary"""
    return {
        'id': entry.idseq,
        'kanji_forms': [{
            'text': kf.text,
            'info': kf.info,
            'priority': kf.pri
        } for kf in entry.kanji_forms],
        'kana_forms': [{
            'text': kf.text,
            'info': kf.info,
            'priority': kf.pri,
            'restrictions': kf.restr
        } for kf in entry.kana_forms],
        'senses': [{
            'pos': sense.pos,
            'glosses': [g.text for g in sense.gloss],
            'info': sense.info,
            'field': sense.field,
            'misc': sense.misc,
            'dialect': sense.dialect,
            'source_language': sense.lsource
        } for sense in entry.senses]
    }

def inspect_jmdict_entry(word):
    """Detailed inspection of JMdict entry with JSON output"""
    jam = Jamdict()
    result = jam.lookup(word)
    
    print(f"\n{'='*80}")
    print(f"JMdict information for: {word}")
    print(f"{'='*80}")
    
    if not result.entries:
        print("No entries found")
        return
    
    # Convert entries to JSON-friendly format
    entries_data = [entry_to_dict(entry) for entry in result.entries]
    
    # Print as formatted JSON
    print("\nJSON Structure:")
    print(json.dumps(entries_data, indent=2, ensure_ascii=False))
    
    # Print as Python dict (might be easier to read)
    print("\nPython Dict Structure:")
    pprint(entries_data, width=80, compact=False)

def main():
    # Test with a sample word
    test_words = ['勉', '読', '楽']
    
    for word in test_words:
        inspect_jmdict_entry(word)
        input("\nPress Enter to continue to next word...")
    
    # Interactive mode
    while True:
        word = input("\nEnter a word to inspect (or 'q' to quit): ")
        if word.lower() == 'q':
            break
        inspect_jmdict_entry(word)

if __name__ == "__main__":
    main()