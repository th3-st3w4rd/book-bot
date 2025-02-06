def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        final_word_count = count_words(file_contents)
    print(final_word_count)
    final_character_count = character_count(file_contents)
    print(final_character_count)


def count_words(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return word_count


def character_count(book_text):
    count = {}
    print(type(book_text))
    for letter in book_text.lower():
        if letter not in count.keys():
            count[letter] = 1
        else:
            count[letter] += 1
    return count


main()
