# https://www.python.org/about/help/


from tracemalloc import DomainFilter


DEFAULT_DOMAIN = "goit.ua"
url = input("Enter url: ")
domain = url.split("/")[2]
print("Доменне ім'я: ", domain.replace('www.', ""))


#print(type(url), url, id(url))
