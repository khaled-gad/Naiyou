import json
import genanki
import random
import requests
import re
from jamdict import Jamdict

# Initialize Jamdict
jam = Jamdict()

# Constants
POS_SUBSCRIPT_MAP = {
    'vs': 'スル',
    'n': '名',
    'vi': '自',
    'vt': '他',
    'adj-na': 'な',
    'adj-i': 'い',
    'adv': '副',
    'noun (common) (futsuumeishi)': '名',
    'noun or participle which takes the aux. verb suru': 'スル',
    'intransitive verb': '自',
    'transitive verb': '他',
    'adverb (fukushi)': '副',
    'Godan verb with ru ending': '五段動詞',
    'Ichidan verb': '一段動詞',
}

# Function to get kanji readings from kanji.json
def get_kanji_readings(kanji_char, kanji_data):
    kanji_info = kanji_data.get(kanji_char, {})
    on_yomi = '、'.join(kanji_info.get('readings_on', []))
    kun_yomi = '、'.join(kanji_info.get('readings_kun', []))
    return on_yomi, kun_yomi

# Function to get words containing the kanji
def get_kanji_words(kanji_char, words_data):
    words_list = []
    for word_entry in words_data:
        word_texts = []
        # Get all kanji forms
        for kanji_form in word_entry.get('kanji', []):
            word_texts.append(kanji_form['text'])
        # Get all kana forms (if no kanji form)
        if not word_entry.get('kanji'):
            for kana_form in word_entry.get('kana', []):
                word_texts.append(kana_form['text'])
        # Check if the kanji is in any of the word texts
        contains_kanji = False
        for word_text in word_texts:
            if kanji_char in word_text:
                contains_kanji = True
                break
        if contains_kanji:
            words_list.append(word_entry)
    return words_list

# Function to get part-of-speech subscripts
def get_pos_subscript(pos_list):
    subscripts = []
    for pos in pos_list:
        if pos in POS_SUBSCRIPT_MAP:
            subscripts.append(POS_SUBSCRIPT_MAP[pos])
    return '、'.join(subscripts)

# Function to format common words
def format_common_words(words):
    formatted_words = []
    for word_entry in words:
        # Get the word
        word_text = ''
        reading = ''
        if word_entry.get('kanji'):
            word_text = word_entry['kanji'][0]['text']
            if 'kana' in word_entry and word_entry['kana']:
                reading = word_entry['kana'][0]['text']
        elif word_entry.get('kana'):
            word_text = word_entry['kana'][0]['text']
        else:
            continue  # Skip if no text
        
        # Get the part of speech
        pos_set = set()
        for sense in word_entry.get('sense', []):
            pos_list = sense.get('partOfSpeech', [])
            for pos in pos_list:
                pos_set.add(pos)
        pos_subscript = get_pos_subscript(pos_set)
        
        # Get the meaning
        glosses = []
        for sense in word_entry.get('sense', []):
            for gloss in sense.get('gloss', []):
                if gloss['lang'] == 'eng':
                    glosses.append(gloss['text'])
        meaning = '; '.join(glosses)
        
        # Build word HTML
        word_html = f'''
            <div class="word-item">
                <span class="word-kanji">{word_text}</span>
                <span class="word-reading">（{reading}）</span>
                <span class="word-type">（{pos_subscript}）</span>
                <div class="word-meaning">{meaning}</div>
            </div>
        '''
        formatted_words.append(word_html)
    return '\n'.join(formatted_words)

# Main function to generate the Anki deck
def generate_anki_deck():
    # Load the kanji data
    with open('kanji.json', 'r', encoding='utf-8') as f:
        kanji_data = json.load(f)

    # Load the words data
    with open('words.json', 'r', encoding='utf-8') as f:
        words_json = json.load(f)
        words_data = words_json['words']
        tags_dict = words_json['tags']

    # Create the Anki deck
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(deck_id, 'JOYO Kanji Deck')

    # Define the styling and model
    model_id = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        model_id=model_id,
        name='Kanji Model',
        fields=[
            {'name': 'Kanji'},
            {'name': 'OnYomi'},
            {'name': 'KunYomi'},
            {'name': 'CommonWords'}
        ],
        templates=[{
            'name': 'Kanji Card',
            'qfmt': '''
                <div class="kanji-front">{{Kanji}}</div>
            ''',
            'afmt': '''
                {{FrontSide}}
                <hr id="answer">
                <div class="kanji-back">
                    <div class="kanji-character">{{Kanji}}</div>
                    
                    <div class="readings-section">
                        <div class="reading-box on-yomi">
                            <div class="reading-label">音読み</div>
                            <div class="reading-content">{{OnYomi}}</div>
                        </div>
                        
                        <div class="reading-box kun-yomi">
                            <div class="reading-label">訓読み</div>
                            <div class="reading-content">{{KunYomi}}</div>
                        </div>
                    </div>

                    <div class="common-words-section">
                        <div class="section-label">常用例</div>
                        <div class="words-content">{{CommonWords}}</div>
                    </div>
                </div>
            ''',
        }],
        css='''
            .card {
                font-family: "Hiragino Kaku Gothic Pro", "Arial Unicode MS", sans-serif;
                font-size: 20px;
                text-align: center;
                color: #333;
                background-color: #2f2f2f;
                padding: 20px;
            }
            
            .kanji-front {
                font-size: 120px;
                margin: 40px 0;
                color: #ffffff;
            }
            
            .kanji-back {
                color: #ffffff;
            }
            
            .kanji-character {
                font-size: 80px;
                margin: 20px 0;
            }
            
            .readings-section {
                margin: 20px 0;
                font-size: 24px;
                line-height: 1.5;
            }
            
            .reading-box {
                background-color: #3a3a3a;
                border-radius: 10px;
                padding: 15px;
                margin: 10px 40px;
            }
            
            .reading-label {
                color: #888;
                font-size: 16px;
                margin-bottom: 5px;
            }
            
            .reading-content {
                color: #fff;
            }
            
            .common-words-section {
                margin: 30px 40px;
                text-align: left;
                background-color: #3a3a3a;
                border-radius: 10px;
                padding: 20px;
            }
            
            .section-label {
                color: #888;
                font-size: 16px;
                margin-bottom: 15px;
            }
            
            .word-item {
                margin: 10px 0;
                padding: 5px;
                border-bottom: 1px solid #4a4a4a;
            }
            
            .word-kanji {
                font-size: 24px;
                color: #fff;
            }
            
            .word-reading {
                color: #aaa;
                margin-left: 5px;
            }
            
            .word-type {
                color: #888;
                font-size: 0.8em;
                margin-left: 5px;
                padding: 1px 4px;
                border: 1px solid #888;
                border-radius: 3px;
            }
            
            .word-meaning {
                color: #ff69b4;
                margin-left: 10px;
            }
        '''
    )

    # Get the list of JOYO kanji from the kanji data
    joyo_kanji_list = list(kanji_data.keys())

    for kanji_char in joyo_kanji_list:
        # Get kanji readings
        on_yomi, kun_yomi = get_kanji_readings(kanji_char, kanji_data)
        
        # Get words containing the kanji
        words_list = get_kanji_words(kanji_char, words_data)
        # Sort words: common words first
        words_list_sorted = sorted(words_list, key=lambda x: not any(k.get('common', False) for k in x.get('kanji', []) + x.get('kana', [])))
        # Limit to 10 words
        words_list_sorted = words_list_sorted[:10]
        # Format common words
        common_words_html = format_common_words(words_list_sorted)
        
        # Create note
        note = genanki.Note(
            model=my_model,
            fields=[kanji_char, on_yomi, kun_yomi, common_words_html]
        )
        my_deck.add_note(note)

    # Save the deck
    genanki.Package(my_deck).write_to_file('joyo_kanji.apkg')
    print("Anki deck 'joyo_kanji.apkg' has been created successfully.")

if __name__ == '__main__':
    generate_anki_deck()