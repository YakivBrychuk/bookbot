import sys
from stats import get_book_text, words_count, count_unq_char, sort_dict

def main():
    file_path = sys.argv[1]
    # file_path = "books/frankenstein.txt"    
    content = get_book_text(file_path)
    words_count(content) # get the words count

    dict_unq = count_unq_char(content)

    sorted_char = sort_dict(dict_unq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count(content)} total words")
    print("--------- Character Count -------")

    for char in sorted_char:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ================")

if len(sys.argv) != 2:

    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()