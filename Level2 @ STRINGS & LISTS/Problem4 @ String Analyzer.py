text = "Python is awesome for data science"

# 1. Print the length of the string
print("The length of text is", len(text))

# 2. Print it in uppercase
print("Uppercased:", text.upper())

# 3. Print it in lowercase
print("Lowercase:", text.lower())

# 4. Print the first 6 characters
print("First 6 Character", text[:7])

# 5. Print the last 6 characters
print("Last 6 Character", text[-6:])

# 6. Count how many times 'a' appears
print("'a' appears in the sample text is", text.count("a"), "Times.")

# 7. Replace 'awesome' with 'powerful'
print("Changed new word 'powerful' in the place of 'awesome':\n", text.replace('awesome', 'powerful'))

# 8. Split into list of words
print("Splitted sample text:", list(text.split()))