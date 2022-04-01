# ----------* CHALLENGE 80 *----------
# Ask the user to enter their first name and then display the length of their first name.
# Then ask for their surname and display the length of their surname. Join their first
# name and surname together with a space between and display the result. Finally, 
# display the length of their full name (including the space).

first_name = input("Enter your first name: ")
len_firstName = len(first_name)
print("Your first name has",len_firstName,"letters")

surname = input("Enter your surname: ")
len_surname = len(surname)
print("Your surname has",len_surname,"letters")

name = [first_name, surname]
name_space = ' '.join(name)
len_name = len(name_space)
print(name_space)
print("Your complete name has",len_name,"letters")