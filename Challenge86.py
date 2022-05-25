# ----------*CHALLENGE 086 ----------*
# Ask the user to enter a new password. Ask them to enter it again. If the two passwords
# match, display “Thank you”. If the letters are correct but in the wrong case, display the
# message “They must be in the same case”, otherwise display the message “Incorrect”.


password = input("Enter your password: ")
confirmation_pw = input("Enter again your password: ")

if password == confirmation_pw:
    print("Thank you!")
elif password != confirmation_pw:
    pw1_lowcase = password.lower()
    pw2_lowcase = confirmation_pw.lower()
    if pw1_lowcase == pw2_lowcase:
        print("They must be in the same case")
    else:
        print("Incorrect")