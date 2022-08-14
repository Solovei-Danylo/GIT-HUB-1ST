# Варіант від ментора без методів зовсім...))
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if "a" <= ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        encoded_message = encoded_message + new_char
    elif "A" <= ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message = encoded_message + new_char
    else:
        encoded_message = encoded_message + ch
print(encoded_message)
