articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key: str, letter_case: bool = False):
    my_list = []

    if letter_case:
        for item in articles_dict:
            if (key in item['title']) or (key in item['author']):
                my_list.append(item)

    else:
        key = key.lower()
        for i in articles_dict:

            if (key in str(i['title']).lower()) or (key in str(i['author']).lower()):
                my_list.append(i)

    return my_list
