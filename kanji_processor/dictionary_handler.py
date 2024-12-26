# kanji_processor/dictionary_handler.py
from jamdict import Jamdict
import requests

class DictionaryHandler:
    def __init__(self):
        self.jam = Jamdict()
        self.kanji_cache = {}  # Cache for kanji readings
        self.pos_mapping = {
            'noun (common) (futsuumeishi)': '名',
            'noun or participle which takes the aux. verb suru': 'する',
            'verb': '自',
            'intransitive verb': '自',
            'transitive verb': '他',
            'i-adjective': 'い',
            'na-adjective': 'な',
            'adverb (fukushi)': '副'
        }

    def get_word_info(self, word):
        """Get word information from JMdict"""
        results = self.jam.lookup(word)
        if not results.entries:
            return {'reading': '', 'type': '', 'meaning': ''}
        
        entry = results.entries[0]
        
        # Get reading
        reading = ''
        if entry.kana_forms:
            reading = entry.kana_forms[0].text
        
        # Get type and meaning from first sense
        word_type = ''
        meaning = ''
        if entry.senses:
            sense = entry.senses[0]
            word_type = self._determine_type(sense.pos)
            meaning = '; '.join(g.text for g in sense.gloss)
        
        return {
            'reading': reading,
            'type': word_type,
            'meaning': meaning
        }

    def get_kanji_readings(self, kanji):
        """Get only kanji readings from kanjiapi.dev"""
        # Check cache first
        if kanji in self.kanji_cache:
            return self.kanji_cache[kanji]

        try:
            response = requests.get(f"https://kanjiapi.dev/v1/kanji/{kanji}")
            if response.status_code == 200:
                data = response.json()
                readings = {
                    'on_yomi': ', '.join(data.get('on_readings', [])),
                    'kun_yomi': ', '.join(data.get('kun_readings', []))
                }
                # Cache the result
                self.kanji_cache[kanji] = readings
                return readings
        except Exception as e:
            print(f"Error fetching kanji readings for {kanji}: {str(e)}")
        
        return {
            'on_yomi': '',
            'kun_yomi': ''
        }

    def _determine_type(self, pos_tags):
        """Determine word type from POS tags"""
        if not pos_tags:
            return ''
        
        if 'noun or participle which takes the aux. verb suru' in pos_tags:
            return 'する'
        
        for tag in pos_tags:
            if tag in self.pos_mapping:
                return self.pos_mapping[tag]
        
        return ''