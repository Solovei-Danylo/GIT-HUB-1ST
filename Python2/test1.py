text = "Hi there Billy! How are you? Where are you from?+-=!@#$%^&*()_+"

alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
char_set = set()
punct_set = set()

for SOMES in text:
    if SOMES.lower() in alphabet:
        char_set.add(SOMES)
    else:
        punct_set.add(SOMES)
print("chars: ", char_set)
print("symbols: ", punct_set)
