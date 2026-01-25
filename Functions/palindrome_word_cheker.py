def is_palindrome(word):
    lower_word = word.casefold()
    return lower_word == lower_word[::-1]


word = input("Please enter a word: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
