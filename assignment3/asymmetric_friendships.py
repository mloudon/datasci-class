import sys
import MapReduce
from collections import Counter

mr = MapReduce.MapReduce()

def mapper(record):
    # key: personA
    # value: number of friends
    key = record[0]
    friend = record[1]
    mr.emit_intermediate(friend, key)
    mr.emit_intermediate(key, friend)

def reducer(key, list_of_values):
    # key: personA
    # list_of_values: list friend relations including that person
    cnt = Counter(list_of_values)
    for friend in cnt.elements():
        if cnt[friend] == 1:
            mr.emit((key,friend))


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)