import sys, os
import pandas as pd 
from collections import defaultdict

def number_to_words(phoneNum):
	inverse_phone_dict = {"a":"2", "b": "2", "c": "2",
						"d": "3", "e": "3", "f": "3",
						"g": "4", "h": "4", "i": "4",
						"j": "5", "k": "5", "l": "5",
						"m": "6", "n": "6", "o": "6",
						"p": "7", "q": "7", "r": "7","s": "7",
						"t": "8", "u": "8", "v": "8",
						"w": "9", "x": "9", "y": "9", "z": "9",
						}
	words_df = pd.read_csv(os.path.join(sys.path[0], 'words.csv'))
	print(os.path.join(sys.path[0], 'words.csv'))

if __name__ == "__main__":
	number_to_words("1-800-724-6837")
