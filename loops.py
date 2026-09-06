# ==========================================
# PYTHON LOOPS PRACTICE PROGRAM
# ==========================================

while True:

    print("\n========== PYTHON LOOPS ==========")
    print("1. Print numbers 1 to 10")
    print("2. Print even numbers")
    print("3. Print odd numbers")
    print("4. Multiplication table")
    print("5. Sum of numbers")
    print("6. Factorial")
    print("7. Check prime number")
    print("8. Countdown")
    print("9. Break example")
    print("10. Continue example")
    print("11. Star pattern")
    print("12. Reverse number")
    print("0. Exit")
    print("===================================")

    choice = int(input("Enter your choice: "))

    # 1. Print numbers 1 to 10
    if choice == 1:

        for i in range(1, 11):
            print(i)


    # 2. Even numbers
    elif choice == 2:

        for i in range(1, 21):
            if i % 2 == 0:
                print(i)


    # 3. Odd numbers
    elif choice == 3:

        for i in range(1, 21):
            if i % 2 != 0:
                print(i)


    # 4. Multiplication table
    elif choice == 4:

        num = int(input("Enter a number: "))

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)


    # 5. Sum of numbers
    elif choice == 5:

        num = int(input("Enter a number: "))

        total = 0

        for i in range(1, num + 1):
            total = total + i

        print("Sum =", total)


    # 6. Factorial
    elif choice == 6:

        num = int(input("Enter a number: "))

        factorial = 1

        for i in range(1, num + 1):
            factorial = factorial * i

        print("Factorial =", factorial)


    # 7. Prime number
    elif choice == 7:

        num = int(input("Enter a number: "))

        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print("Prime number")
        else:
            print("Not a prime number")


    # 8. Countdown
    elif choice == 8:

        num = int(input("Enter starting number: "))

        while num >= 1:
            print(num)
            num = num - 1

        print("Finished!")


    # 9. Break
    elif choice == 9:

        for i in range(1, 11):

            if i == 6:
                break

            print(i)

        print("Loop stopped!")


    # 10. Continue
    elif choice == 10:

        for i in range(1, 11):

            if i == 5:
                continue

            print(i)


    # 11. Star pattern
    elif choice == 11:

        for i in range(1, 6):
            print("*" * i)


    # 12. Reverse number
    elif choice == 12:

        num = int(input("Enter a number: "))

        reverse = 0

        while num > 0:

            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        print("Reverse =", reverse)


    # Exit
    elif choice == 0:

        print("Program closed.")
        break


    else:

        print("Invalid choice. Please try again.")