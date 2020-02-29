def words_to_number(wordifiedNum):
	#Mapping from letters to numbers
	letter_dict = {"A":"2", "B": "2", "C": "2",
						"D": "3", "E": "3", "F": "3",
						"G": "4", "H": "4", "I": "4",
						"J": "5", "K": "5", "L": "5",
						"M": "6", "N": "6", "O": "6",
						"P": "7", "Q": "7", "R": "7","S": "7",
						"T": "8", "U": "8", "V": "8",
						"W": "9", "X": "9", "Y": "9", "Z": "9",
						}
	#All dashes in wordified number replaced with empty char and predefined dash locations set
	num = wordifiedNum.replace('-', '')
	dashes = [1, 5, 9]

	#Replace letters with numbers using the dictionary
	for ch in letter_dict.keys():
		num = num.replace(ch, letter_dict.get(ch))

	#Place dashes are the predefined locations
	for i in dashes:
		num = num[:i] + '-' + num[i:]

	print(num)
	return num

if __name__ == "__main__":
	words_to_number("1-CAB-QUANTUM")


