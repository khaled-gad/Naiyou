# kanji_processor/utils/db_handler.py
import sqlite3
import json

class DatabaseHandler:
    def __init__(self, db_path='kanji.db'):
        self.db_path = db_path
        self.setup_database()
    
    def setup_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS kanji (
                    kanji TEXT PRIMARY KEY,
                    on_yomi TEXT,
                    kun_yomi TEXT,
                    common_words TEXT,
                    frequency INTEGER
                )
            ''')
            conn.commit()
    
    def save_kanji_data(self, kanji_data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO kanji 
                (kanji, on_yomi, kun_yomi, common_words, frequency)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                kanji_data['kanji'],
                json.dumps(kanji_data['on_yomi']),
                json.dumps(kanji_data['kun_yomi']),
                json.dumps(kanji_data['common_words']),
                kanji_data['frequency']
            ))
            conn.commit()