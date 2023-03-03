from mapreduce import MapReduce
import re
#-----------------------------------

class CharCount(MapReduce):

    def mapper(self, _, line):
        for char in line:
            yield (char,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

#-----------------------------------
#Input file name
input_filename = 'InputTxt'
#read-only format
fob = open(input_filename+".txt",'r')
data = fob.read()
#using re package
#get only a to z
inputdata = re.sub('[^A-Za-z]','',data)
#handle new line 
inputdata = re.sub('\n+','\n',inputdata).upper()
#handle tabs
inputdata = re.sub('\t+','\t',inputdata)
#display data
outputdata = CharCount.run(inputdata)
for item in outputdata:
    print(item)
