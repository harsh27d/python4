#Sum of highest and lowest frequency 
def sumofFrequency(arr):
    d={}
    for x in arr:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    high=0
    low= len(arr)
    for x in d:
        
        if d[x]>high:
            high=d[x]
        if d[x]<low:
            low=d[x]
    return high+low
