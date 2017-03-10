lists = [['quick', 'slow'], ['brown', 'red', 'blue'], ['fox', 'dog']]

def goIn(current, next):
    if not next:
        print current
        return
    words = next[0]
    for word in words:
        new_current = current + ' ' + word
        goIn(new_current, next[1:])

goIn('', lists)




def conc(base, next):
	if not next:
		print base
		return
	for word in next[0]:
		conc(base + ' ' + word, next[1:])

conc('', lists)

