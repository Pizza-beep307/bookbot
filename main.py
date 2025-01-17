import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = characters_app(text)
    #print(f"{num_words} words found in the document")
    #print(num_characters)
    reporte = report(characters_app(text))
    print(reporte)
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def characters_app(text):
    number_of_times_dict = {}
    for i in text.lower():
        if i in number_of_times_dict:
            number_of_times_dict[i] += 1
        else:
            number_of_times_dict[i] = 1
    return number_of_times_dict    

def report(dictionnary):
    chain_report = "--- Begin report of books/frankenstein.txt ---"
    for letter in dictionnary:
        if letter in "abcdefghijklmnopqrstuvwxyz" :
            chain_report += f"\nThe '{letter}' character was found {dictionnary[letter]} times" 
    return chain_report

main()

