# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.
from collections import defaultdict

def print_anagrams(paragraph):
    words = paragraph.split()
    grouped_words = defaultdict(list)

    for word in words:
        # Sort the characters in the word and join them back into a string
        sorted_word = "".join(sorted(word))
        grouped_words[sorted_word].append(word)

    # Print all anagrams together
    for group in grouped_words.values():
        if len(group) >=1: # Only print if there are one pr more  than one anagram
            print(" ".join(group))

# Test the function
print_anagrams("race car  god act")



