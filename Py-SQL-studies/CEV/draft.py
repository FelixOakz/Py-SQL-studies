def split_and_join(line):
    n = line.replace(' ', '-')
    return n
    
if __name__ == '__main__':
    line = input('this is a string')
    result = split_and_join(line)
    print(result)