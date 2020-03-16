# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000


# w = 0
# rim = input("please enter letter: ")
# for t in rim:
#     if t == 'I':
#         w += 1
#     elif t == 'V':
#         w = V-1 
#     elif t == 'X':
#         w = X-1  
#     elif t == 'L':
                
# print(w)


def roman_to_int(s):
    x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    w = 0
    #print(range(len(s)))
    for i in range(len(s)):
        #print(x[s[i]])
        #print(i)
        if i > 0 and x[s[i]] > x[s[i - 1]]:
         #   print(x[s[i-1]])
            w += x[s[i]] - 2 * x[s[i - 1]]
          #  print(w)
        else:
            w += x[s[i]]
    return w

print(roman_to_int('IV'))
print(roman_to_int('MCMXCIV'))
print(roman_to_int('III'))