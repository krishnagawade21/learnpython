# Function to calculate sum of digits

def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


# Main program
number = int(input("Enter a number: "))

result = sum_of_digits(number)

print("Sum of digits:", result)