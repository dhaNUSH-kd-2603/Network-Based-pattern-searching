# search.py
import re

class Search:
    def __init__(self, filename="sample.txt"):
        self.filename = filename
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            raise Exception(f"File '{self.filename}' not found!")

    def clean(self):
        """Remove special characters using regex."""
        cleaned_lines = []
        for line in self.lines:
            # Keep only alphanumeric and spaces
            cleaned_line = re.sub(r'[^A-Za-z0-9\s]', '', line)
            cleaned_lines.append(cleaned_line.strip())
        self.lines = cleaned_lines

    def getLines(self, word):
        """Return list format: [word, (line_no, text), ...]"""
        results = [word]
        for i, line in enumerate(self.lines, start=1):
            if word.lower() in line.lower():
                results.append((i, line.strip()))
        return results
