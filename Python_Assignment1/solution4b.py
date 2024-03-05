"""
importing wrapper function from decorators
"""
from package import decorators
@decorators.log
def reverse(string):
    """
    Split the input string into a list of words
    """
    words = string.split()
    # Initialize an empty list to store the reversed words
    reversed_words = []
    # Iterate over the indices of the words list in reverse order
    for i in range(len(words) - 1, -1, -1):
        # Append each word to the reversed_words list in reverse order
        reversed_words.append(words[i])
    # Join the reversed words back into a string with spaces
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

input_sentence = input("Enter the sentence: ")
OUTPUT = reverse(input_sentence)
print(OUTPUT)