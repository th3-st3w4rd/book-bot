def main():
    book_path = "books/frankenstein.txt"
    file_contents, file_word_count = get_text(book_path)
    final_character_count = character_count(file_contents)
    stats_in_order = sort_stats(final_character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{file_word_count} words found in the document")

    for letter in stats_in_order:
        letter_value = letter["letter"]
        if letter_value.isalpha():
            count = letter["count"]
            print(f"The '{letter_value}' character was found {count} times.")
    print("--- End report ---")


def get_text(book):
    with open(book) as f:
        file_contents = f.read()
        final_word_count = count_words(file_contents)
        return file_contents, final_word_count


def count_words(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return word_count


def character_count(book_text):
    count = {}
    for letter in book_text.lower():
        if letter not in count.keys():
            count[letter] = 1
        else:
            count[letter] += 1
    return count


def sort_by_alpahbet(dict_item):
    return dict_item["count"]


def sort_stats(stats):
    sort_list = []
    for pairs in stats:
        sort_list.append({"letter": pairs, "count": stats[pairs]})
    sort_list.sort(reverse=True, key=sort_by_alpahbet)
    return sort_list


main()
