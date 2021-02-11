# 1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

words = ["hello", "hey","goodbye", "yo", "yes", "Elephant"]

for word in words:
    print(word.upper())

# 2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(list):
    """
    print out each word on a separate line, but in all uppercase

    """

    for word in list:
        print (word.upper())

 # print_upper_words(words)


# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def print_upper_words(list):
    """
    print out each word that starts with the letter 'e'

    """

    for word in list:
        if word[0].lower() == 'e':
            print (word.upper())


# print_upper_words(words)

# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words(list, must_start_with):
    """
    print out each word that starts with the letters passed in

    """
    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "elephant"], must_start_with={"e", "h"})
