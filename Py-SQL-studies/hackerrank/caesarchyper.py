alpha = 'abcdefghijklmnopqrstuvwxyz'
s = 'middle-Outz'
rot = 2
for letter in s:
    if letter.isalpha():
        if letter.islower():
            loc = (alpha.find(letter) + rot) % 26
            print(f'{alpha[loc]}', end='')
        else:
            letter = letter.lower()
            loc = (alpha.find(letter) + rot) % 26
            print(f'{alpha[loc].upper()}', end='')
    else:
        print(f'{letter}', end='')
