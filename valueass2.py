def countOddNumbers(n,arr):
    count=0
    for i in arr:
        if i%2!=0:
            count+=i
    return count
