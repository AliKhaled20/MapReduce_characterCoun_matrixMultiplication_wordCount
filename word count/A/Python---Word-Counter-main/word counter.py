print("Hello user the program is easy, All you need to do is input a sentence.")
sentence = input(str("Please enter a sentence: "))

# Important to convert all possible upper case words to lower case
# Note: new sentence in lower case is lower_sentence
lower_sentence = sentence.lower()

# Returns the total word length of the user's lower case sentence, which was split into a list
word_total = len(lower_sentence.split())

print("\nThe sentence contains a total of " + str(word_total) + " words.")


# Important to ignore special characters which will affect word frequency
# List of defined special characters
special_characters = ['!', '#', '$', '%', '&', '@', '[', ']', '.', '_', '?', '(', ')', '{', '}', '=', ',']
converted_sentence = ''.join(filter(lambda i:i not in special_characters, lower_sentence))

print("\nNew sentence without any special characters: ", converted_sentence)


# Function for calculating word frequency in sentence
def word_frequency(str):
    # Use dict because objects are ordered, changeable and do not allow duplicates
    frequency = dict()
    words = str.split()

    # for loop to check for frequency of word duplicates
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

print("\nThe following is the word frequency: ")
print(word_frequency(converted_sentence))
