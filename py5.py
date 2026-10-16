#Sum of array element
def sum_of_array_elements(n,arr):
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    return sum