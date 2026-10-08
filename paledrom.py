def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")