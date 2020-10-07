#!/usr/bin/python3
import argparse, json, sys

#dictionaryFile = 'words_dictionary.json'
dictionaryFile = 'websters_dictionary.json'


def matchString(dict, string):

	stringDict = list(string)
	results = []

	#remove spaces from dict
	for word in dict:
		if " " in word:
			word = word.replace(" ", "")

		#convert current word into a list
		wordList = list(word)

		#iterate over user input
		for char in stringDict:
			if char in word:
				debugPrint(f"{char} in {word}")
				#remove each match from the word list
				try:
					wordList.remove(char)
				except Exception as ex:
					debugPrint(f"Unable to remove {char} from {word} with current wordlist {wordList}")

		#if the wordlist is empty then we have a match
		if len(wordList) == 0:
			results.append(word)

	return results

def debugPrint(string):
	if args.debug:
		print(string)

#Main thread
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'A utility to generate solutions to Wordscapes')
	parser.add_argument('-l', '--letters', help = 'The letters from the current puzzle')
	parser.add_argument('-d', '--debug', action='store_true', help = 'Whether to enable debug outputs or not')
	args = parser.parse_args()

	if args.letters is None:
		print("Please enter the characters (with the -l or --letters command) from your current puzzle and try again!")
		sys.exit(0)

	#Load dictionary into memory
	with open(dictionaryFile) as f:
		englishDict =json.load(f)

	#Call string match
	solution = matchString(englishDict, args.letters)

	#remove single char matches
	solution = [i for i in solution if len(i) > 1]

	print(json.dumps(solution))
