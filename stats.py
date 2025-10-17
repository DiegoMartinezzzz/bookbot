def get_book_text(file_path):
    with open(file_path, 'r') as file:
        file_text =  file.read()
        
    return file_text

def each_char_counter(file_text):
    char_dict = {}

    for character in file_text:
        char = character.lower()
        if char.isalpha() == True:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] = char_dict[char] + 1

    return char_dict

def sort_on(list_to_sort):
    return list_to_sort["num"]
    
def sorted_list_creator(char_dict):
    sorted_list =[]

    for key in char_dict:

        sorted_list.append({
        "name" : key,
        "num" : char_dict[key]
        })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


    
