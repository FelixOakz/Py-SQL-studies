alpha = 'abcdefghijklmnopqrstuvwxyz'
s = 'middle-Outz'
rot = 2

for letter in s:
    if letter.isalpha():
        if letter.islower():
            loc = alpha.find(letter)
            loc += rot
            print(letter, alpha[loc])
        else:
            letter = letter.lower()
            loc = alpha.find(letter)
            loc += rot
            print(letter, alpha[loc].upper())
    else:
        print(letter)