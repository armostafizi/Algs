def is_one_away(s1, s2):
    # s2 is longer or the same size
    if len(s2) - len(s1) > 1:
        return False
    i1 = 0; i2 = 0
    error = False
    for i in range(len(s1)):
        if s1[i1] == s2[i2]:
            i1 += 1; i2 += 1
            continue;
        if error:
            return False
        error = True
        if len(s1) == len(s2):
            i1 += 1
        i2 += 1;
    return True


s1 = raw_input()
s2 = raw_input()

if len(s2) > len(s1):
    print is_one_away(s1, s2)
else:
    print is_one_away(s2, s1)

