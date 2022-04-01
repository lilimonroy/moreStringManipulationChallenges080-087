# ----------* CHALLENGE 82 *----------
# Show the user a line of text from your favourite poem and ask for a starting and ending point. 
# Display the characters between those two points.

poem_fragment= "With this field-dew consecrate, every fairy take his gait;"
print(poem_fragment)
start = int(input("Enter a start point: "))
end = int(input("Enter a end point: "))

print(poem_fragment[start:end+1])