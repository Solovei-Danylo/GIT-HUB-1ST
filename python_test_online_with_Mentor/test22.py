"""Напишите программу, которая принимает текст
 и выводит два слова: наиболее часто 
 встречающееся и самое длинное.
"""

text = 'lorem ipsum dolor sit amet amet amet halalalv'


def search_somes(text):
    text = text.split(" ")
    print(text)
    count = 0
    word = None
    for item in text:
        item_count = text.count(item)
        if item_count > count:
            count = item_count
            word = item
    print(count, word)


# print(search_somes(text))

search_somes(text)
