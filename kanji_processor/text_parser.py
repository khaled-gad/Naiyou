# kanji_processor/text_parser.py
import fugashi
import re
from .utils.name_filter import NameFilter

class JapaneseTextParser:
    def __init__(self):
        self.tagger = fugashi.Tagger()
        self.name_filter = NameFilter()
        
    def extract_kanji(self, text):
        kanji_pattern = r'[一-龯]'
        return re.findall(kanji_pattern, text)
    
    def tokenize_text(self, text):
        words = self.tagger(text)
        return [word for word in words 
                if not self.name_filter.is_name(word.surface)]
    
    def extract_words_with_kanji(self, text):
        tokens = self.tokenize_text(text)
        kanji_words = []
        for token in tokens:
            if any(self.is_kanji(char) for char in token.surface):
                # Debug print to see available features
                # print(dir(token.feature))
                kanji_words.append({
                    'word': token.surface,
                    'reading': token.feature.kana if hasattr(token.feature, 'kana') else '',
                    'pos': token.feature.pos1,
                    'pos_detail': token.feature.pos2
                })
        return kanji_words
    
    @staticmethod
    def is_kanji(char):
        return '\u4E00' <= char <= '\u9FFF'