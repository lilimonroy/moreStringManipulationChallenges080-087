# ----------*CHALLENGE 085 ----------*
# Ask the user to type in their name and then tell them how many vowels are in their name.

name = input("Enter your name: ")
vowels_dictionary = {}

name = name.lower()

for vowel in "aeiou": #Declare the vowels
    count_volwels = name.count(vowel)  #Count vowels and then
    vowels_dictionary[vowel] = count_volwels  #add to the dictionary

total_vowels = sum(vowels_dictionary.values()) #Sum the values of each vowel in the name

print("Your name has", total_vowels, "vowels:",vowels_dictionary)