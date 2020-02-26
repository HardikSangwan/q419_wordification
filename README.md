# q419_wordification

Demo Project for Pickle Robot Company
The Project implements the three function below:

1. numbers_to_words: Takes string argument representing US phone number and outputs a wordified phone number. Example: 
Input -> "1-800-724-6837"
Output -> "1-800-PAINTER"

2. words_to_numbers: Reverse of above. Example:
Input -> "1-800-724-6837"
Output -> "1-800-PAINTER"

3. all_wordifications: Outputs all possible combinations of numbers and words in a given phone number

#Requirements

Code written in Python 3.7.5. Install requirements using pip install -r requirements.txt

#Execution

Run python main.py with the following arguments to execute the functions:

-> --wordify for numbers_to_words followed by number to wordify. Example:
	python main.py --wordify 1-800-724-6837
-> --numerify for words_to_numbers followed by wordified number to reverse. Example:
	python main.py --numerify 1-800-PAINTER
-> --all for all_wordifications followed by number.

All functions output strings to console.

#Solution Overview

Used the following unix words file as the English words dictionary: https://gist.github.com/wchargin/8927565.

numbers_to_words: Check for longest word that will fit into the number based on the words list above.

words_to_numbers: Simply iterates over input string and replaces letters with corresponding numbers using a dictionary. For example 'A' and 'B' and 'C' would all map to 2.

all_wordifications: Build a dictionary with all possible contiguous substrings of the phone number as keys and all possible words combinations for that substring as the values for that particular key.

#Assumptions
Dash locations for a 'non-wordified' phone number always follow the pattern "1-111-111-1111". So dashes at indexes 1, 5 and 9.




