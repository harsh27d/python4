#Count vowel in a string 
def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count+=1
    return count 
print(count_vowels("haaarsh"))
