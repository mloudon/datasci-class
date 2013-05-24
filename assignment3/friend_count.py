import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: personA
    # value: number of friends
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents that word occurs in
    mr.emit((key, len(list_of_values)))


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)