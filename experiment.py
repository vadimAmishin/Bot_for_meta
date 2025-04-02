nn = []
while True:
    n = input()
    if n == '':
        break
    nn.append(n)
sp = {}
print(nn)
for i in range(len(nn)):
    nn[i] = nn[i].split(':')[0]

    if i % 2 == 0 and nn[i] in sp:
        sp[nn[i]] += nn[i + 1]
    elif i % 2 == 0:
        sp[nn[i]] = nn[i+1]

print(sp)