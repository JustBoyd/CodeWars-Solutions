def solution(args):
    i = 0
    while i < len(args):
        j = i 
        while j + 1 < len(args) and args[j] + 1 == args[j + 1]:
            j += 1
        if j != i and j - i > 1:
            args[i:j+1] = [f"{args[i]}-{args[j]}"]
        i += 1
    return ",".join(map(str, args))