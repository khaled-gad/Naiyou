# setup.py
from setuptools import setup, find_packages

setup(
    name="kanji-deck-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'fugashi',
        'unidic-lite',
        'jamdict',
        'jamdict-data',
        'genanki',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'generate-kanji-deck=kanji_processor.cli:main',
        ],
    },
    author="",
    author_email="your.email@example.com",
    description="A tool to generate Anki decks from Japanese text with kanji information",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kanji-deck-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)