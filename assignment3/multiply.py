import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: position in matrix c = a %*% b - a(i)b(j)
    # value: (j,value) for a, (i, value) for b
    matrix=record[0]
    i = record [1]
    j = record [2]
    value=record[3]
    
    if matrix=="a":
        for col in [0,1,2,3,4]:
            mr.emit_intermediate("%d,%d"%(i,col),(j,value))

    elif matrix=="b":
        for row in [0,1,2,3,4]:
            mr.emit_intermediate("%d,%d"%(row,j),(i,value))
        

def reducer(key, list_of_values):
    # key: (row,col) in c
    # values: pairs or numbers to be multiplied together
    values_to_multiply = {}
    
    for tuple in list_of_values:
        if tuple[0] not in values_to_multiply:
            values_to_multiply[tuple[0]]= []
        values_to_multiply[tuple[0]].append(tuple[1])
        
    
    result = 0;   
    for mult_key in values_to_multiply.keys():
        if len(values_to_multiply[mult_key])==2:
            result += (values_to_multiply[mult_key][0]*values_to_multiply[mult_key][1])
            
    split = key.split(",")
    row = int(split[0])
    col = int(split[1])
        
    mr.emit((row,col,result))
    
    
    
    


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)