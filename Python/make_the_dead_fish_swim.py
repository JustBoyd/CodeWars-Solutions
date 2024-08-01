def parse(data):
    value = 0
    arr = []
    comm = list(data)
    
    for i in range(len(comm)):
        if(comm[i] == 'i'):
            value += 1
        elif(comm[i] == 'd'):
            value -= 1
        elif(comm[i] == 's'):
            value = value ** 2
        elif(comm[i] == 'o'):
            arr.append(value)
    return arr