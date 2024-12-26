# kanji_processor/anki_generator.py
import genanki
import random

class AnkiDeckGenerator:
    def __init__(self):
        # Create a unique model ID and deck ID
        self.model_id = random.randrange(1 << 30, 1 << 31)  # This creates a large random number
        self.model = genanki.Model(
            model_id=self.model_id,  # Add model_id= explicitly
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
                            <div class="on-yomi">
                                {{OnYomi}}
                            </div>
                            
                            <div class="kun-yomi">
                                {{KunYomi}}
                            </div>
                        </div>

                        <div class="common-words-section">
                            {{CommonWords}}
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
                
                .on-yomi {
                    margin: 10px 0;
                }
                
                .kun-yomi {
                    margin: 10px 0;
                }
                
                .common-words-section {
                    margin: 30px 0;
                    text-align: left;
                }
                
                .word-item {
                    margin: 10px 0;
                    font-size: 20px;
                    line-height: 1.6;
                }
                
                .word-reading {
                    color: #cccccc;
                }
                
                .word-meaning {
                    color: #ff69b4;
                    margin-left: 10px;
                }

                .word-type {
                    color: #808080;
                    font-size: 0.8em;
                    margin-left: 5px;
                    padding: 1px 4px;
                    border: 1px solid #808080;
                    border-radius: 3px;
                }
            '''
        )
    
    def format_common_words(self, words):
        """Format common words with proper HTML structure"""
        formatted_words = []
        for word, details in words:
            # Create the word type tag if it exists
            word_type = details.get('type', '')
            type_html = f'<span class="word-type">（{word_type}）</span>' if word_type else ''
            
            word_html = f'''
                <div class="word-item">
                    {word} <span class="word-reading">({details.get('reading', '')})</span>
                    {type_html}
                    <span class="word-meaning">{details.get('meaning', '')}</span>
                </div>
            '''
            formatted_words.append(word_html)
        return '\n'.join(formatted_words)

    def generate_deck(self, kanji_data, deck_name="Kanji Deck"):
        deck_id = random.randrange(1 << 30, 1 << 31)
        deck = genanki.Deck(deck_id, deck_name)
        
        for kanji_info in kanji_data:
            note = genanki.Note(
                model=self.model,
                fields=[
                    kanji_info['kanji'],
                    kanji_info['on_yomi'],
                    kanji_info['kun_yomi'],
                    self.format_common_words(kanji_info['common_words'])
                ])
            deck.add_note(note)
        
        return deck
    
    def save_deck(self, deck, filename="kanji_study.apkg"):
        """Save the deck to an Anki package file"""
        try:
            genanki.Package(deck).write_to_file(filename)
            print(f"Successfully saved deck to {filename}")
        except Exception as e:
            print(f"Error saving deck: {e}")