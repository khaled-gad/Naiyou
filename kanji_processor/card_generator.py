# kanji_processor/card_generator.py
class CardGenerator:
    def __init__(self, db_handler):
        self.db_handler = db_handler
    
    def generate_card(self, kanji_data):
        return {
            'front': kanji_data['kanji'],
            'back': self._format_back(kanji_data)
        }
    
    def _format_back(self, kanji_data):
        return {
            'on_yomi': kanji_data['on_yomi'],
            'kun_yomi': kanji_data['kun_yomi'],
            'common_words': [
                {
                    'word': word['word'],
                    'reading': word['reading'],
                    'pos': word['pos'],
                    'frequency': word['frequency']
                }
                for word in kanji_data['common_words']
            ]
        }