# Arabic Spelling Mistake Analysis

Arabic Spelling Mistake Analysis is a project focused on detecting common spelling errors in Arabic words using a custom-built algorithm. The system compares input words against a predefined list of correct terms, identifying likely mistakes based on character differences and linguistic patterns. It offers valuable insights for improving text input accuracy and can be adapted for educational tools or automated correction systems.

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

