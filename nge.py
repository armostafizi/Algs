a = raw_input('Numbers?')
a = [int(x) for x in a.split()]
nges = []

for i, j in enumerate(a):
    nge = -1
    for k in a[i+1:]:
        if k > j:
            nge = k
            break
    nges.append(nge)

print nges
