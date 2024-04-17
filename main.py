

# Reads the contents of the file
def get_book_text(path):
    with open(path) as f:
        return f.read()



# Takes the text from the book as a string, then returns the number of words in that string.
def get_word_count(text):
    words_list = text.split()
    return len(words_list)


# Takes the text from the book as a string, converts all characters to lowercase, and returns the number of times each character appears in the string.
# Use a dictionary in the format: String -> Integer
def get_character_dict(text):
    chars = {}
    for c in text:
        lowercase = c.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars


def sort_on(d):
    return d["num"]

# Convert character dictionary into a list of dictionaries sorted in descending order.
def sort_dict_desc(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list


# Print only letters in the sorted list
def print_letters_sorted(list):
    for item in list:
        if not item["char"].isalpha():
            continue
        print(f"The letter '{item['char']}' was found {item['num']} times in the document")





def main():

    # Book path
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    numwords = get_word_count(text)
    chars_dict = get_character_dict(text)
    sorted_dict = sort_dict_desc(chars_dict)

    print(f"---Begin report of {book_path}---")
    print()

    print(f"There are {numwords} words in the document.")
    print()


    print_letters_sorted(sorted_dict)
    print()

    print(f"---End report of {book_path}---")





if __name__ == "__main__":
    main()
