import string

def words(text):
    word = text.split()
    return (len(word))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_cnt(chars1):
    counter = 0
    req_dict = {}
    chars = chars1.lower()
    alphabet = list(string.ascii_lowercase)
    for i in range(0, len(alphabet)):
        for j in range(0, len(chars)):
            if alphabet[i] == chars[j]:
                counter +=1
        req_dict[alphabet[i]] = counter
        counter = 0
    return req_dict     


def main():
    
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
       

    count = words(file_contents)
    
    char_count = char_cnt(file_contents)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")

    list_char =list(char_count)
    for char in list_char:
        print(f"The {char} character was found {char_count[char]} times")
    
    print("--- End report ---")



main()