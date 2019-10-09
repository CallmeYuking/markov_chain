"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    new_text_string = open(file_path)

    return new_text_string.read()


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    
    chains = {}
    # for i in range(len(words)-2):
    #     ngram = (words[i], words[i+1], words[i+2])
        
    #     chains[ngram] = chains.get(ngram, [])

    #     if i < (len(words)-3):
    #         chains[ngram].append(words[i+3])
       # words[i+2]
    for i in range(len(words)-(n-1)):

 #   print(chains)

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key_list = sorted(chains.keys())

    next_key = choice(key_list)
    words.extend(next_key)
    
    while chains[next_key] != [] and len(words) < 200:
    # for pair in key_list:
        words.append(choice(chains[(next_key)]))
        next_key = tuple(words[-3:])
     #   print(next_key)

  #  words.append(choice(chains[(next_key)]))
  #  next_key = tuple(words[-2:])

  #  print(words)
   # print(third_key)


    # your code goes here

    return " ".join(words)

    


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
