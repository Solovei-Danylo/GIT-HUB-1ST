num = int(input("Enter a number: "))

if num > 0:
    if num >= 100:
        result = "Positive High!!! number"
    else:
        result = "Positive mid number"
elif num < 0:
    result = "Negative number! Cannot be used it! "
else:
    result = "It is zero, please insert your number correctly! "
print(result)
