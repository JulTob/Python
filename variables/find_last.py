def find_last(where,what):
    if where.find(what)==-1:
            return -1
    index=0
    total=-1
    while index>=0:
            total=index
            index=where.find(what,index+1)
    return total
