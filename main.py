book = "books/frankenstein.txt"

def count_words_in_book(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
    return word_count

def count_characters(filename):
    character_count_dict = {}


    with open(filename, "r") as file:
        text = file.read()
        lowered_text = text.lower()
        unique_characters = set(lowered_text)

        for character in unique_characters:
            character_count = 0
            for letter in lowered_text:
                if letter == character:
                    character_count += 1
            character_count_dict[character] = character_count

    return character_count_dict

def dict_to_list_of_dicts(dictionary):
    return [{key: value} for key, value in dictionary.items()]

def sort_on(dictionary):
    return dictionary["character"]

def main():
    word_count = count_words_in_book(book)
    character_list = dict_to_list_of_dicts(count_characters(book))
    character_list.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")


main()