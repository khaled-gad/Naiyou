import json

def find_joyo_coverage():
    # Load Joyo kanji
    with open('inputs/kanji-jouyou.json', 'r', encoding='utf-8') as f:
        joyo_kanji = set(json.load(f).keys())
    
    seen_kanji = set()
    total_needed = len(joyo_kanji)
    last_percentage = 0
    
    # Validate Joyo kanji count
    if total_needed > 2200:  # Sanity check - should be around 2136
        print("Warning: Unexpected number of Joyo kanji loaded")
        return None
    
    print(f"Starting scan - Need to find {total_needed} unique Joyo kanji")
    print("-" * 50)
    
    with open('input_text.txt', 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Extract only kanji that are in Joyo list
            kanji_in_line = {c for c in line.strip() if c in joyo_kanji}
            new_kanji = kanji_in_line - seen_kanji
            seen_kanji.update(kanji_in_line)
            
            # Calculate coverage percentage
            current_percentage = (len(seen_kanji) * 100) // total_needed
            
            # Print progress when finding new kanji
            if new_kanji:
                print(f"Line {line_num:>6}: Found {len(seen_kanji):>4}/{total_needed} Joyo kanji ({current_percentage}%)")
                print(f"         New kanji: {''.join(new_kanji)}")
            
            if seen_kanji.issuperset(joyo_kanji):
                print("-" * 50)
                print(f"✓ Found all Joyo kanji at line {line_num}")
                return line_num
    
    missing = joyo_kanji - seen_kanji
    print("-" * 50)
    print(f"✗ Missing {len(missing)} kanji:")
    print(''.join(sorted(missing)))
    return None

if __name__ == "__main__":
    result = find_joyo_coverage()