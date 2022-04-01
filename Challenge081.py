# ----------* CHALLENGE 81 *----------
# Ask the user to type in their favourite school subject.
# Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.

favoriteSubject = input("Enter your favorite subject: ")
for letter in favoriteSubject:
    print(letter, end='-')