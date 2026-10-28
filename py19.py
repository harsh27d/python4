def palindrome(n):
    if str(n) == str(n)[::-1]:
        return("is palandrome")
    else:
        return("no palandrome")

print(palindrome(121))
    