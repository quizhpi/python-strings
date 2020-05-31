#
# Strings with python
#

# \n adds new line
print("Hello\nNextLine")

# Escape character
print("Hello, I\'m John")

# Converting string to lowercase
phrase = "My name is John"
print(phrase.lower())

# Converting string to uppercase
comment = "I did it!!!"
print(comment.upper())

# Check if string is in uppercase
comment = "I don\'t know"
print(comment.upper().isupper())

# Check how many character in the string
comment = "How many is there?"
print(len(comment))

# Output the first character of the string
comment = "Checking"
print(comment[0])

# Returns the index of a specific character in a string
comment = "Working"
print(comment.index("k"))

# Replace function - substring is replaced with another substring
comment = "Last word"
print(comment.replace("word", "chance"))
