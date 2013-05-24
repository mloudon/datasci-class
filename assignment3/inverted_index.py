import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents that word occurs in
    results = set (list_of_values)
    mr.emit((key, list(results)))


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)