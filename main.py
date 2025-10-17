from stats import get_book_text, each_char_counter, sorted_list_creator, sort_on
import sys 

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage:$ python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(book_path)

    print(f"Found {work_counter(book_text)} total words")

    char_dict_result = each_char_counter(book_text)

    sorted_list = sorted_list_creator(char_dict_result)
    
    for element in sorted_list:
        print(f"{element["name"]}: {element["num"]}")



def work_counter(file_text):
    words_in_file_text = file_text.split()

    return len(words_in_file_text)

main()
