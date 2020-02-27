import os, sys

letter_dict = {"A":"2", "B": "2", "C": "2",
						"D": "3", "E": "3", "F": "3",
						"G": "4", "H": "4", "I": "4",
						"J": "5", "K": "5", "L": "5",
						"M": "6", "N": "6", "O": "6",
						"P": "7", "Q": "7", "R": "7","S": "7",
						"T": "8", "U": "8", "V": "8",
						"W": "9", "X": "9", "Y": "9", "Z": "9",
						}

def let_to_num(word):
	for ch in letter_dict.keys():
		word = word.replace(ch, letter_dict.get(ch))
	return word


def number_to_words(num):
	#Remove Dashes. Add Back later
	num = num.replace('-','')
	wordifiedNum = num
	dashes = [1, 5, 9]

	#English Words Dictionary
	engDict = []
	with open(os.path.join(sys.path[0],"words.csv")) as f:
		engDict = f.readlines()
	engDict = [w.rstrip().upper() for w in engDict]

	possWords = filter(lambda word: let_to_num(word) in num, engDict)
	possWords = sorted(list(possWords), key = len)

	for word in possWords: 
		wordNum = let_to_num(word)
		wordifiedNum = num.replace(wordNum, word)

	for i in dashes:
		if wordifiedNum[i-1] not in letter_dict.keys():
			wordifiedNum = wordifiedNum[:i] + '-' + wordifiedNum[i:]

	print(wordifiedNum)
	return wordifiedNum