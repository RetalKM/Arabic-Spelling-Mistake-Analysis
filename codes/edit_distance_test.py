#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 08:59:29 2023

@author: areejalsini
"""
import pyarabic.araby as araby
from nltk.metrics.distance import edit_distance

def spell_check(word):
    # Check if the word is valid Arabic
    if not araby.is_arabicrange(word):
        return [word]

    # Generate a list of similar words based on edit distance
    similar_words = [w for w in words if edit_distance(word, w) <= 2]
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
        