# 1 . Write a program to read a file and count how many vowels are present in its content.
f = open("sample2.txt", "r")
content = f.read()
vowels = "aeiouAEIOU"
count = 0
for char in content:
    if char in vowels:
        count += 1
print("Total number of vowels:", count)
f.close()
