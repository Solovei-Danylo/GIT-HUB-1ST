def real_len(text):
    for exc in ('\n', '\f', '\r', '\t', '\v'):
        text = text.replace(exc, '')

    return len(text)


print(real_len('Alex\nKdfe23\t\f\v.\rвввввввввв'))
