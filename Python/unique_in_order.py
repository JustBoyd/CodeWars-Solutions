def unique_in_order(sequence):
    ls = list(sequence)
    res = []
    var = None
    
    for x in ls:
        if x != var:
            res.append(x)
        var = x
    return res