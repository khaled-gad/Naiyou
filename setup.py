# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
            'pre-commit>=3.0.0',
            'black>=23.0.0',
            'isort>=5.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'generate-kanji-deck=kanji_processor.cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to generate Anki decks from Japanese text with kanji information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kanji-deck-generator",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/kanji-deck-generator/issues",
        "Documentation": "https://yourusername.github.io/kanji-deck-generator/",
        "Source Code": "https://github.com/yourusername/kanji-deck-generator",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Japanese",
    ],
    python_requires='>=3.6',
    keywords="japanese, kanji, anki, flashcards, language-learning",
)