def is_palindrome(sent):
    alpha_numberic = ""

    for char in sent:
        if char.isalnum():
            alpha_numberic += char
    
    alpha_numberic_lower = alpha_numberic.casefold()

    return alpha_numberic_lower == alpha_numberic_lower[::-1]

sentence = input("Please enter a sentence: ")

if is_palindrome(sentence):
    print(f"'{sentence}' is a palindrome")
else:
    print(f"'{sentence}' is not a palindrome")
