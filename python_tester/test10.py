import re


def find_word(text, word):
    match_object = re.search(word, text)
    return {
        'result': bool(match_object),
        'first_index': match_object.span[0] if match_object else None,
        'last_index': match_object.span[1] if match_object else None,
        'search_string': word,
        'string': text
    }
