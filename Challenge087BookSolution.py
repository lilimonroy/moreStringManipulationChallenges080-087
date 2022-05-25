# ----------*CHALLENGE 087 ----------*
# Ask the user to type in a word and then display it backwards on separate lines. 
# For instance, if they type in “Hello” it should display as shown below:
#            Enter a word: Hello
#               o
#               l
#               l
#               e
#               H


from turtle import position


word = input("Enter a word: ")
lengh = len(word) # In case of 'Hello' is 5
num = 1
for every_letter in word:
    position = lengh - num # With this operation we have the new reverse position of the letter
    letter = word[position] # We replace the letter. Npw H is in the last position.
    print(letter) #Display the letter in its new position
    num = num + 1 # It's time to the next letter.  
