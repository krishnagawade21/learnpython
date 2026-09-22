numbers = [10, 25, 7, 45, 18, 32]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("List:", numbers)
print("Largest number:", largest)