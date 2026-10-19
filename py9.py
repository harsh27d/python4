#PGM for largest odd number in a string 
def largest_odd_number(s:str) -> str:
    for i in range(len(s)-1, -1, -1):
        if int(s[i])%2!=0:
            return int(s[:i+1])