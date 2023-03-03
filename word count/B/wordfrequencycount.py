#!/usr/bin/python

from mapreduce import MapReduce

class WordFrequencyCount(MapReduce):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)

class WordCount(MapReduce):

    def mapper(self, _, line):
        for word in line.split():
            yield (word,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

class CharCount(MapReduce):

    def mapper(self, _, line):
        for char in line:
            if char != ' ':
                yield (char,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':

    print("Hello user the program is easy, All you need to do is input a sentence.")
    sentence = input(str("Please enter a sentence: "))

    output = WordFrequencyCount.run(sentence)


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
    print(word_frequency(sentence))

    # for item in output:
    #    print (item)

