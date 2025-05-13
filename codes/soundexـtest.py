#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 09:09:39 2023

@author: areejalsini
"""
"""

pip install fuzzywuzzy
pip install jellyfish


"""


import pyarabic.araby as araby
from fuzzywuzzy import fuzz
import jellyfish

def soundex(word):
    return jellyfish.soundex(word)

def spell_check(word):
    # Check if the word is valid Arabic
    if not araby.is_arabicrange(word):
        return [word]

    # Generate a list of similar words based on edit distance and Soundex
    similar_words = []
    for w in words:
        if fuzz.ratio(word, w) >= 80 or soundex(word) == soundex(w):
            similar_words.append(w)

    return similar_words

# Test the spell_check function
text = "هذا مثااال للتحقق من الإملاء."
tokens = araby.tokenize(text)

# List of Arabic words for reference
words = [
    "هذا", "مثال", "للتحقق", "من", "الإملاء"
    # Add more words here if needed
]

for token in tokens:
    suggestions = spell_check(token)
    if suggestions:
        print(f"Spelling mistake: {token}. Suggestions: {suggestions}")