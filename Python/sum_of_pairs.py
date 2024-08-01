def sum_pairs(ints, s):
    dict = {}
    
    for i in ints:
        if i in dict:
            return [s-i, i]
        else: dict[s-i] = i
        
    return