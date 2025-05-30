# kanji_processor/anki_generator.py
import genanki
import random
from kanji_processor.utils.extract_joyo import JOYO_KANJI

class AnkiDeckGenerator:
    def __init__(self):
        self.model_id = random.randrange(1 << 30, 1 << 31)
        self.model = genanki.Model(
            model_id=self.model_id,
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
                
                .word-reading {
                    color: #aaa;
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
    def is_joyo_kanji(self, kanji):
        """Check if kanji is in Joyo set."""
        return kanji in JOYO_KANJI
    
    def format_common_words(self, words):
        """Format common words with proper HTML structure"""
        formatted_words = []
        for word, details in words[:10]:
            word_html = f'''
                <div class="word-item">
                    {word} <span class="word-reading">({details.get('reading', '')})</span>
                    <span class="word-type">（{details.get('type', '')}）</span>
                    <span class="word-meaning">{details.get('meaning', '')}</span>
                </div>
            '''
            formatted_words.append(word_html)
        return '\n'.join(formatted_words)

    def generate_deck(self, kanji_data, deck_name="Kanji Deck"):
            deck_id = random.randrange(1 << 30, 1 << 31)
            deck = genanki.Deck(deck_id, deck_name)
            
            skipped_kanji = []
            processed_kanji = []
            
            for kanji_info in kanji_data:
                kanji = kanji_info['kanji']
                
                # Only create card if kanji is Joyo
                if self.is_joyo_kanji(kanji):
                    note = genanki.Note(
                        model=self.model,
                        fields=[
                            kanji,
                            kanji_info['on_yomi'],
                            kanji_info['kun_yomi'],
                            self.format_common_words(kanji_info['common_words'])
                        ])
                    deck.add_note(note)
                    processed_kanji.append(kanji)
                else:
                    skipped_kanji.append(kanji)
            
            # Print summary
            print(f"\nDeck Generation Summary:")
            print(f"Processed {len(processed_kanji)} Joyo kanji")
            print(f"Skipped {len(skipped_kanji)} non-Joyo kanji")
            if skipped_kanji:
                print(f"Skipped kanji: {''.join(skipped_kanji)}")
            
            return deck

    
    def save_deck(self, deck, filename="kanji_study.apkg"):
        """Save the deck to an Anki package file"""
        try:
            genanki.Package(deck).write_to_file(filename)
            print(f"Successfully saved deck to {filename}")
        except Exception as e:
            print(f"Error saving deck: {e}")