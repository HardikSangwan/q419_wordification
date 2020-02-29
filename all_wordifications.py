import os, sys

#Mapping from letters to numbers.
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
	#Return word converted into number using mapping.
	for ch in letter_dict.keys():
		word = word.replace(ch, letter_dict.get(ch))
	return word

def dashes_fix(wordifiedNum):
	#Fix Dashes in new wordified US Phone number
	wordifiedNum = list(wordifiedNum)
	dashes = [1, 5, 9]
	for i in dashes:
		if wordifiedNum[i-1] not in letter_dict.keys():
			wordifiedNum = wordifiedNum[:i] + ['-'] + wordifiedNum[i:]

	if wordifiedNum[-1] == '-':
		wordifiedNum[-1] = ''
	i = 1
	while i < len(wordifiedNum):
		if (wordifiedNum[i-1] == '-' and wordifiedNum[i] == '-'):
			wordifiedNum = wordifiedNum[:i-1] + [''] + wordifiedNum[i:]
		i = i + 1
	#if wordifiedNum[1] != '-':
	#	wordifiedNum =  wordifiedNum[:1] + ['-'] + wordifiedNum[1:]

	wordifiedNum = "".join(wordifiedNum)
	return wordifiedNum


def all_wordifications(num):
	#Remove Dashes from number. Add Back later
	num = num.replace('-','')
	if len(num) != 11:
		return "Invalid Phone Number"
	wordifiedNum = num

	#Import English Words Dictionary
	engDict = []
	with open(os.path.join(sys.path[0],"words.csv")) as f:
		engDict = f.readlines()
	engDict = [word.rstrip().upper() for word in engDict]

	#List of Possible words for the number sorted by length
	possWords = filter(lambda word: let_to_num(word) in num, engDict)
	possWords = sorted(list(possWords), key = len)

	#Print wordified numbers from list of possible words
	print(dashes_fix(num))
	for word in possWords: 
		wordifiedNum = num.replace(let_to_num(word), '-' + word + '-')
		wordifiedNum = dashes_fix(wordifiedNum)
		print(wordifiedNum)

	return wordifiedNum

if __name__ == "__main__":
	all_wordifications("1-230-000-0000")