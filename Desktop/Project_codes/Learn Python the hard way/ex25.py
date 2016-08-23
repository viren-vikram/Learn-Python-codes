def break_words(stuff):
	"""this is the breakup words function"""
	words=stuff.split(' ')
	return words
	
def sort_words(words):
	"""sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	""" prints the first wotrjafter popping it off"""
	word = words.pop(0)
	print(word)

def print_last_words(words):
	""" this will print the last word after popping it off"""
	word=words.pop(-1)
	print (word)
	
def sort_sentence(sentence):
	""" this is a full sentence and returned the sorted words"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_words(words)
	
def print_firstandlast(sentence):
	"""print first and last word of the sentence"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_words(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_words(words)	

