def solution(s):
    split = [*s]
    
    if(len(split) == 0):
        return split
    elif(len(split) % 2) != 0:
        last = split[-1]
        lst = [''.join(split[i:i+2]) for i in range(0, len(split), 2)]
        lst[-1] = last + "_" 
        return lst
    else:
        lst1 = [''.join(split[i:i+2]) for i in range(0, len(split), 2)]
        return lst1 
    pass