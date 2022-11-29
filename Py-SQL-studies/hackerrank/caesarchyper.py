alpha = 'abcdefghijklmnopqrstuvwxyz'
s = 'middle-Outz'
rot = 2

for i in s:
    loc = alpha.find(i)
    s.replace(i, alpha[loc])