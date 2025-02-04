# Function 1     Task 11

def is_palindrome(word):
    if word == ''.join(reversed(word)):
        print("It's Palindrome")
    else:
        print("It's not Palindrome")

word = str(input())
is_palindrome(word)