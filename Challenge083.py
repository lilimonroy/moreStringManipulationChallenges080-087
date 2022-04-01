# ----------* CHALLENGE 83 *----------
# Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. 
# Keep repeating this until they type in a message all in uppercase.

word = input("Enter a word in upper case: ")
word_uppercase = True

if word.isupper():
    print(print("The word",word,"is upper case."))
else:
    word_uppercase = False
    while word_uppercase == False:
        word = input("The last word wasn't in upper case. Try enter the word again: ")
        if word.isupper():
            word_uppercase = True
            print("The word",word,"is upper case.") 
        else:
            word_uppercase = False
            break 





