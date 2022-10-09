# Напишите программу,
# которая принимает имя файла и выводит
# его расширение. Если расширение у файла определить
# невозможно, выбросите исключение.


documents = "archivezip.txt"


def analis_extension(documents: str):
    documents_new = documents.split(".")
    if len(documents_new) < 2:
        raise ValueError("Please enter again")
    first, *middle, last = documents_new
    print(first, middle, last)
    return last


print(analis_extension(documents))
