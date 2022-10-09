def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 3
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
