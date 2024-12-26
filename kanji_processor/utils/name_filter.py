# kanji_processor/utils/name_filter.py
class NameFilter:
    def __init__(self):
        # This is a simplified version. In practice, you'd want to use
        # a proper names dictionary or API
        self.common_name_kanji = {'田', '山', '川', '村', '木', '本', '佐'}
    
    def is_name(self, word):
        # Simple implementation - would need to be more sophisticated
        # in a production environment
        return (
            any(kanji in word for kanji in self.common_name_kanji) and
            len(word) <= 4  # Most Japanese names are 2-4 characters
        )