# ----------*CHALLENGE 087 ----------*
# Ask the user to type in a word and then display it backwards on separate lines. 
# For instance, if they type in “Hello” it should display as shown below:
#            Enter a word: Hello
#               o
#               l
#               l
#               e
#               H


word = input("Enter a word: ")

reversed_string = ''.join(reversed(word)) # El método join() fusiona todos los caracteres resultantes de la iteración inversa en una nueva cadena.int(reversed_string)

for letter in reversed_string:
    print(letter)