# kanji_processor/dictionary_handler.py
from jamdict import Jamdict

class DictionaryHandler:
    def __init__(self):
        self.jam = Jamdict()
        # Updated POS mapping based on actual API responses
        self.pos_mapping = {
            'noun (common) (futsuumeishi)': '名',
            'noun or participle which takes the aux. verb suru': 'する',
            # "Godan verb with 'mu' ending": '他',  # Most godan verbs are 他動詞
            'transitive verb': '他',
            'intransitive verb': '自',
            'adjective (keiyoushi)': 'い',    # i-adjective
            'adjectival nouns or quasi-adjectives': 'な',  # na-adjective
            'adverb (fukushi)': '副'
        }
    
    def get_word_info(self, word):
        results = self.jam.lookup(word)
        if not results.entries:
            return {'reading': '', 'type': '', 'meaning': ''}
        
        entry = results.entries[0]
        
        # Get reading from kana_forms
        reading = entry.kana_forms[0].text if entry.kana_forms else ''
        
        # Get first sense
        if not entry.senses:
            return {'reading': reading, 'type': '', 'meaning': ''}
        
        sense = entry.senses[0]
        
        # Get type from POS tags
        word_type = self._determine_type(sense.pos)
        
        # Get meaning (join all glosses from first sense)
        meaning = '/'.join(g.text for g in sense.gloss)
        
        return {
            'reading': reading,
            'type': word_type,
            'meaning': meaning
        }
    
    def _determine_type(self, pos_tags):
        """Determine word type from POS tags"""
        if not pos_tags:
            return ''
        
        # Check for する verb first
        if 'noun or participle which takes the aux. verb suru' in pos_tags:
            return 'する'
        
        # Check for other types
        for tag in pos_tags:
            if tag in self.pos_mapping:
                return self.pos_mapping[tag]
        
        # Handle verbs
        if any('verb' in tag.lower() for tag in pos_tags):
            if any('transitive' in tag.lower() for tag in pos_tags):
                return '他'
            if any('intransitive' in tag.lower() for tag in pos_tags):
                return '自'
            return '他'  # default for verbs we're unsure about
        
        # Default to noun if nothing else matches
        if any('noun' in tag.lower() for tag in pos_tags):
            return '名'
            
        return ''