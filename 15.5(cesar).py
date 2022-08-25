alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
s = input().split()
x = ''
for i in s:
    step = 0
    for j in i:
        if j.isalpha() == True:
            step += 1
    for j in i:
        text = alph.find(j)
        new = text + step
        if j.isalpha() == True:
            x += alph[new]
        else:
            x += j
    x += ' '
print(x)