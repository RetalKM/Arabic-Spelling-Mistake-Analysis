#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:37:24 2023

@author: areejalsini
"""
import pandas as pd
import pyarabic.araby as araby
from nltk.metrics.distance import edit_distance

def spell_check(word):
    # Check if the word is valid Arabic
    if not araby.is_arabicrange(word):
        return [word]

    # Generate a list of similar words based on edit distance
    similar_words = [w for w in words if edit_distance(word, w) <= 2]
    return similar_words


# Load the DataFrame from a CSV file
df = pd.read_csv('rockstargames1.csv' ,encoding='utf-8')

# List of Arabic words for reference
words = [
    "هذا", "مثال", "للتحقق", "من", "الإملاء"
    # Add more words here if needed.--------------------------###important step..These words are just examples..
]



# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Access the string value in a specific column
    # Test the spell_check function
    #text = row
    # Convert the Series to text
    text = row.to_string(index=False)
    print (text)
    tokens = araby.tokenize(text)
    for token in tokens:
        suggestions = spell_check(token)
        if suggestions:
            print(f"Spelling mistake: {token}. Suggestions: {suggestions}")
    
    # Perform operations with the string value
    # ...
