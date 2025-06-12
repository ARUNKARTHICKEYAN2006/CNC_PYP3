# Read the input file
with open("input.txt", "r") as file:
    text = file.read()

# Remove punctuation manually
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_text = ""
for char in text:
    if char not in punctuations:
        clean_text += char

# Convert to lowercase and split into words
words = clean_text.lower().strip().split()

# Count words without using get()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

# Write to output file
with open("output.txt", "w") as file:
    for word in word_count:
        file.write(word + ": " + str(word_count[word]) + "\n")
