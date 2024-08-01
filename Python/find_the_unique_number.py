def find_uniq(arr):
    for i in range(len(arr)):
        for x in range(len(arr)):
            if arr[x] != arr[i] and arr[x] != arr[i-1]:
                return arr[x]