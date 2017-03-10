import string
import random

with open('test_str.txt', 'w') as f:
    for i in range(5000):
        line = ''
        for j in  range(1000):
            char = random.choice(string.ascii_lowercase)
            line += char * random.randint(1, 30)
        f.write(line + '\n')
