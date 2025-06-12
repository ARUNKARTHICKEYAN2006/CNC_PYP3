import os

# Step 1: Create input.txt if it doesn't exist
if not os.path.exists("input.txt"):
    with open("input.txt", "w") as file:
        file.write("Hello world! This is a test. Hello again, world.")

# Step 2: Read the contents
with open("input.txt", "r") as file:
    text = file.read()

# Step 3: Process text and strip punctuation
words = text.split()
clean_words = [word.strip(".,!?") for word in words]

# Step 4: Count word frequencies
word_counts = {}
for word in clean_words:
    word = word.lower()  # Optional: make case-insensitive
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Step 5: Write to output.txt without f-strings
with open("output.txt", "w") as out_file:
    for word in word_counts:
        out_file.write(word + ": " + str(word_counts[word]) + "\n")

print("Word count written to output.txt.")
