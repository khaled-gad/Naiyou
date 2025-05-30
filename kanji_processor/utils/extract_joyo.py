import json
from pathlib import Path

def load_joyo_kanji():
    # Navigate up two levels from utils/ to project root, then to inputs/
    json_path = Path(__file__).parent.parent.parent / 'inputs' / 'kanji-jouyou.json'
    with open(json_path, 'r', encoding='utf-8') as file:
        kanji_data = json.load(file)
        return list(kanji_data.keys())

JOYO_KANJI = load_joyo_kanji()