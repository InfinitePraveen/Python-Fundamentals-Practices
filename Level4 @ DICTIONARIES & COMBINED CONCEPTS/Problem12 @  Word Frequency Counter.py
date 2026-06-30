text = """the quick brown fox jumps over the lazy dog the fox 
          is quick the dog is lazy"""

# 1. Split the text into words
# .split() automatically handles multiple spaces and newlines
words = text.split()

# 2 & 3. Count how many times each word appears and store in a dictionary
word_counts = {}
for word in words:
    # Convert to lowercase to ensure 'The' and 'the' are treated the same (optional but recommended)
    word = word.lower() 
    
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# 4. Print the dictionary
print("Word Counts:")
print(word_counts)
print("-" * 30)

# 5. Find the most common word
most_common_word = None
highest_count = 0

for word, count in word_counts.items():
    if count > highest_count:
        highest_count = count
        most_common_word = word

print(f"The most common word is '{most_common_word}' with a count of {highest_count}.")