def num_words(book):
	words = book.split()
	total = len(words)
	return total

def num_letters(book):
	lowercase = book.lower()
	lower_words = lowercase.split()
	char_dict = {}
	for word in lower_words:
		letters = list(word)
		for l in letters:
			if l in char_dict:
				char_dict[l] += 1
			else:
				char_dict[l] = 1
	return char_dict

def sort_on(items):
	return items["num"]

def sort_dicts(dict):
	values = []
	for k in dict:
		new_dict = {"letter" : k, "num" : dict[k]}
		values.append(new_dict)
		new_dict = {}
	values.sort(reverse=True, key=sort_on)
	return values