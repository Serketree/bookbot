import sys
from stats import num_words
from stats import num_letters
from stats import sort_dicts

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	full_text = get_book_text(sys.argv[1])
	letter_dict = num_letters(full_text)
	letter_list = sort_dicts(letter_dict)
	word_count = num_words(full_text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words.")
	print("--------- Character Count -------")
	for d in letter_list:
		temp_list = []
		for k in d:
			temp_list.append(d[k])
		if temp_list[0].isalpha():
			print(f"{temp_list[0]}: {temp_list[1]}")
	print("============= END ===============")
	return

main()