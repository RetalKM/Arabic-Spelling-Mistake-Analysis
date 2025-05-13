# Project Overview

This project focuses on detecting common spelling mistakes in Arabic words using a custom-built algorithm. The solution compares input words to a predefined list of correct words and identifies likely mistakes based on character mismatches and linguistic patterns. It provides insights for improving text input accuracy and can be adapted for educational or correctional purposes.


# Features

	• Compares user input with a reference dataset of correct Arabic words.
	• Detects character-level differences such as substitutions, insertions, and deletions.
	• Outputs suggested corrections or flags input as incorrect.
	• Lightweight and adaptable for further development.


# Technologies Used

	• Python
	• Standard libraries (e.g., difflib, re)
	• Custom logic (no third-party spellcheck libraries used)

#  How It Works
 
	1. Loads a reference dataset of valid Arabic words.
	2. Accepts user input for a word to check.
	3. Compares the input to dataset entries using a custom matching algorithm.
	4. Outputs suggestions based on similarity score.

 # How to Run
 
 1. Clone the repository:
 git clone https://github.com/RetalKM/Arabic-Spelling-Mistake-Analysis.git
cd Arabic-Spelling-Mistake-Analysis

 2. Make sure you have Python installed (version 3.6 or later).
 3. Run the main script: python spelling_checker.py
 4. Follow the on-screen instructions to input a word and receive suggestions.

