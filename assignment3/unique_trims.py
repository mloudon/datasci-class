import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: sequence id
    # value: string of nucleotides
    key = record[0]
    value = record[1]
    short_value=value[0:len(value)-10]
    mr.emit_intermediate("1", short_value)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents that word occurs in
    results = set(list_of_values)
    for item in results:
        mr.emit(item)


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)