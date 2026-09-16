def check_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if check_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")