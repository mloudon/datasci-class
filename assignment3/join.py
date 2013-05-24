import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: common id
    # value: all records (both types) with the common id
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: common id
    # value: list of all records with the common id
    orders=[]
    items=[]
    for record in list_of_values:
        if record[0] == "order":
            orders.append(record)
        elif record[0] == "line_item":
            items.append(record)
    
    for order in orders:
        for item in items:
            mr.emit(order+item)


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)