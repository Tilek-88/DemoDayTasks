
def removeVowels(word):
    g = word[::-1]
    num = ('a', 'e', 'o', 'u')
    for c in word:
        if c.lower() in num:
            if c == 'a':
                word = word.replace(c,"0")
            elif c == 'e':
                word = word.replace(c, '1')    
    return g, word, word+'aca'

print(removeVowels('apple'))