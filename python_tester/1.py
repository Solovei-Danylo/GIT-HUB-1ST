
numbers = [1, 2, 3, 4, 5, 6, -7, -8, -9, -10]
new_numbers = []


for number in numbers:
    if abs(number) >= 5:
        new_numbers.append(number)
print(new_numbers)


# На вхід дається список з цілих чисел.
# Результатом работи має стати новий список, в якому містяться тільки ті числа, які більше 5 по модулю.
