# ----------*CHALLENGE 084 ----------*
# Ask the user to type in their postcode. Display the first two letters in uppercase.

postcode = input("Enter your postcode: ")

for every_letter in postcode:
    lenght = len(postcode) 
    upperPostcode_1 = postcode[0].upper()
    upperPostcode_2 = postcode[1].upper()
    lowPostcode = (postcode[2:lenght+1])

print (upperPostcode_1 + upperPostcode_2 + lowPostcode) # All the postcode

print (upperPostcode_1 + upperPostcode_2)
