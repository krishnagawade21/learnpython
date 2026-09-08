while True:

    units = int(input("Enter electricity units: "))

    bill = 0

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 400:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)

    print("Your electricity bill is ₹", bill)

    choice = input("Do you want to calculate another bill? (yes/no): ")

    if choice.lower() == "no":
        print("Program ended.")
        break