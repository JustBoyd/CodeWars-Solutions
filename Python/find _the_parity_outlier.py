def find_outlier(integers):
    even = 0
    odd = 0
    
    if integers[0] % 2 == 0:
        even += 1
    else:
        odd += 1
    
    if integers[1] % 2 == 0:
        even += 1
    else:
        odd += 1
    
    if integers[2] % 2 == 0:
        even += 1
    else:
        odd += 1
        
    if even > odd:
        outlier = 1
    else:
        outlier = 0
        
    for x in integers:
        if x % 2 == outlier:
            return x