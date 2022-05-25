# ----------*CHALLENGE 085 ----------*
# Ask the user to type in their name and then tell them how many vowels are in their name.

name = input("Enter your name: ")

name = name.lower()
count_vowel = 0

for vowel in name:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count_vowel = count_vowel + 1

print("Your name has",count_vowel,"vowels")