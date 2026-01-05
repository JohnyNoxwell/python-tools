# Text Analytics Tools

CLI and core utilities for analyzing text.

## Features
- Normalize text
- Word frequency
- Top-N words
- Longest word
- Vowel counting
- Input from file or URL

## Usage

```bash
python cli.py book.txt
python cli.py book.txt --top 20
python cli.py https://www.gutenberg.org/files/1342/1342-0.txt --top 15
```

## Architecture

- core.py — pure functions for text processing

- cli.py — command line interface

- other .py files — experimental / legacy scripts