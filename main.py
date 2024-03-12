def main():
    with open("./books/frankenstein.txt") as book:
        file_contents = book.read()

    create_report(file_contents)

def number_words(book):
    return len(book.split())

def number_characters(book):
    characters = {}

    for char in book:
        lower = char.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

def sort_on(dict):
    return dict["num"]


def make_alpha_list(dict):
    sort_list = []
    
    for char in dict:
        sort_list.append({"char": char, "num": dict[char]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


def create_report(book):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_words(book)} words found in document\n")

    sorted_list = make_alpha_list(number_characters(book))
    for pair in sorted_list:
        if pair["char"].isalpha():
            print(f"The '{pair["char"]}' character was found {pair["num"]} times")


    
main()