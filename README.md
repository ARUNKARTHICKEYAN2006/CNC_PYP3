Program Purpose:
----------------
This Python program reads text from 'input.txt', removes punctuation, counts the frequency of each word, and writes the result into 'output.txt'.

Files Included:
---------------
1. CNC_3.py        - The main Python script.
2. input.txt       - Input file that contains the original text.
3. output.txt      - Output file that stores the word counts.
4. README.txt      - This documentation file.

How It Works:
-------------
1. Checks if 'input.txt' exists. If not, it creates one with sample text.
2. Reads content from 'input.txt'.
3. Splits the content into words.
4. Removes punctuation like '.', ',', '!', '?' from each word.
5. Converts all words to lowercase for consistent counting.
6. Counts the frequency of each word.
7. Writes the word and its count to 'output.txt'.

Example:
--------
If input.txt contains:
Hello world! This is a test. Hello again, world.

Then output.txt will be:
hello: 2
world: 2
this: 1
is: 1
a: 1
test: 1
again: 1

How to Run:
-----------
Make sure Python is installed on your system.

To run the program:
> python CNC_3.py

Notes:
------
- Only basic punctuation (. , ! ?) is removed.
- Word count is case-insensitive.
- All required files must be in the same folder.
