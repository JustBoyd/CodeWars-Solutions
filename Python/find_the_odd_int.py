def find_it(seq):
    for x in seq:
        x_int = seq.count(x) 
        if(x_int % 2) > 0:
            return x