def find_second (string,target):
    index=string.find(target)
    index2=string.find(target,index+1)
    return index2
