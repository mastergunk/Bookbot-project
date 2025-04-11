import sys
from stats import count_words_in_text
from stats import count_characters_in_text
from stats import sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    word_count = count_words_in_text(contents)
    character_count = count_characters_in_text(contents)
    sorted_characters = sorted_list(character_count)
    #print(f"{word_count} words found in the document")
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")


main()

