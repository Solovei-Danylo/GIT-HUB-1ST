text = 'lorem ipsum dolor sit amet amet amet halalalv'


def search_somes(text):
    text = text.split(" ")
    print(text)
    count = 0
    word = None
    count_longest = 0
    words_longest = None
    for item in text:
        item_count = text.count(item)
        if item_count > count:
            count = item_count
            word = item
        item_len = len(item)
        if item_len > count_longest:
            count_longest = item_len
            words_longest = item

    print(count, word, count_longest, words_longest)


# print(search_somes(text))

search_somes(text)
