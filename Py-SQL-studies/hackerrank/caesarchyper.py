l = 'abcdefghijklmnopqrstuvwxyz'
while True:
    for i in l:
       print(i)
       


    for i in s:
        if i == alpha[25]:
            i -= 25
            if s.isupper():
                s = s[i+k].upper()
            if s.islower():
                s = s[i + k]
    return s