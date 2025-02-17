def vowels(string):
    strvowels = []
    for i in string:
        if i in "aeiou":
            strvowels.append(i)
    return strvowels  

commonvowels = []

def main(string1, string2):
    vstr1 = vowels(string1.lower())
    vstr2 = vowels(string2.lower())
    for i in vstr1:
        if i in vstr2:
            commonvowels.append(i)
    return commonvowels 

print(main("hello", "world"))
