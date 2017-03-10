import time
a = range(-500,500)

start_time = time.time()
answers = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i] + a[j] + a[k] == 0:
                answers.append([a[i], a[j], a[k]])
#                print(a[i], a[j], a[k])

print(len(answers))
print ("-- %s seconds --" % (time.time() -start_time))

print '----'

start_time = time.time()
hashTable = dict()

for i in range(len(a)):
    for j in range(i+1, len(a)):
        key = a[i] + a[j];
        if key in hashTable:
            hashTable[key].append((a[i],a[j]))
        else:
            hashTable[key] = [(a[i], a[j])]

answers = list()

for i in a:
    if -i in hashTable:
        for j in hashTable[-i]:
            if i not in j:
                answer = list(j)
                answer.append(i)
                answer = frozenset(answer)
                answers.append(answer)

#for i in list(set(answers)):
#    print list(i)
print len(list(set(answers)))
print ("-- %s seconds --" % (time.time() -start_time))
