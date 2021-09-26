''' num = 2
while num < 100:
    num = num *2
    print(num) '''

''' s = 'hello'
for char in s:
    print(char) '''

''' s = 'xyz'
i = 0
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1 '''

def up_to_vowel(s):
    s = 'hello'
    befor_vowel = ''
    i = 0
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        befor_vowel = befor_vowel + s[i]
        i = i + 1
    return befor_vowel