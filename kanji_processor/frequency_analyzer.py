# kanji_processor/frequency_analyzer.py
from collections import Counter
from .text_parser import JapaneseTextParser

class FrequencyAnalyzer:
    def __init__(self):
        self.parser = JapaneseTextParser()
    
    def analyze_kanji_frequency(self, text):
        kanji_list = self.parser.extract_kanji(text)
        return Counter(kanji_list)
    
    def analyze_word_frequency(self, text):
        words = self.parser.extract_words_with_kanji(text)
        return Counter(word['word'] for word in words)
    
    def get_sorted_kanji(self, text):
        freq = self.analyze_kanji_frequency(text)
        return sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    def get_sorted_words(self, text):
        freq = self.analyze_word_frequency(text)
        return sorted(freq.items(), key=lambda x: x[1], reverse=True)