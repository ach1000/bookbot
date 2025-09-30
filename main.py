# standard library imports
import sys

# local imports
from stats import get_num_words, get_char_counts, sort_char_counts

# reads the entire text of a book from a file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# check command line arguments
if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# read the book text from the given file
book_text = get_book_text(sys.argv[1])

# get number of words and print it
num_words = get_num_words(book_text)
print(f"Found {num_words} total words")

# get character counts and print them sorted
char_counts = get_char_counts(book_text)
for char_count in sort_char_counts(char_counts):
    print(f"{char_count[0]}: {char_count[1]}")
