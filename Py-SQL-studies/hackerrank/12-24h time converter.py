s = str(input('enter time'))

def convert(s):
    if s[-2] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]


print(convert(s))