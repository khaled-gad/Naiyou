# debug_kanji.py
import requests
import json
from pprint import pprint

def inspect_kanji(kanji):
    """Get kanji information from kanjiapi.dev"""
    try:
        response = requests.get(f"https://kanjiapi.dev/v1/kanji/{kanji}")
        if response.status_code == 200:
            kanji_data = response.json()
            
            print(f"\n{'='*80}")
            print(f"Kanji information for: {kanji}")
            print(f"{'='*80}")
            
            # Print formatted JSON
            print("\nJSON Structure:")
            print(json.dumps(kanji_data, indent=2, ensure_ascii=False))
            
            # Print readable format
            print("\nReadable Format:")
            print(f"Kanji: {kanji_data.get('kanji')}")
            print(f"Grade: {kanji_data.get('grade')}")
            print(f"Stroke count: {kanji_data.get('stroke_count')}")
            print(f"Meanings: {', '.join(kanji_data.get('meanings', []))}")
            print(f"Kun readings: {', '.join(kanji_data.get('kun_readings', []))}")
            print(f"On readings: {', '.join(kanji_data.get('on_readings', []))}")
            print(f"Name readings: {', '.join(kanji_data.get('name_readings', []))}")
            print(f"JLPT level: N{kanji_data.get('jlpt')}" if kanji_data.get('jlpt') else "JLPT level: None")
            
        else:
            print(f"Error: Could not fetch data for kanji {kanji}")
            
    except Exception as e:
        print(f"Error processing kanji {kanji}: {str(e)}")

def main():
    # Test with some common kanji
    test_kanji = ['漢', '字', '本', '日', '月']
    
    print("Testing common kanji...")
    for kanji in test_kanji:
        inspect_kanji(kanji)
        input("\nPress Enter to continue to next kanji...")
    
    # Interactive mode
    print("\nEntering interactive mode...")
    while True:
        kanji = input("\nEnter a kanji to inspect (or 'q' to quit): ")
        if kanji.lower() == 'q':
            break
        inspect_kanji(kanji)

if __name__ == "__main__":
    main()