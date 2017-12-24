def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sorted_words(words):
	"""Sort the words."""
	return sorted(words)

def print_first_word(words):
	"""Print the first words after popping it"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print the last words after popping it"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in full sentence and return sorted words"""
	words = break_words(sentence)
	return sorted_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_sorted_first_and_last(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)