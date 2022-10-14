from collections import Counter

text = 'lorem ipsum dolor sit amet amet amet halalaldsdsdsv'


def search_somes(text):
    text = text.split(" ")
    count = Counter(text)
    count2 = count.most_common()[0]
    print(count2)
    longest = max(text, key=len)
    print(longest)


search_somes(text)
