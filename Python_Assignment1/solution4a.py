"""
importing wrapper function from decorators
"""
from package import decorators
@decorators.log
def reverse(string):
    """
    split the input string into list of words
    """
    words = string.split()
    #reverse the words and join them
    output = " ".join(reversed(words))
    return output

input_sentence=input("Enter the sentence: ")
OUTPUT = reverse(input_sentence)
print(OUTPUT)
