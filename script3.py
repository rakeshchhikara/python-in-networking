f = open('configuration.txt')

for x in f:
    print(x, end='')
f.close()
print(f.closed)
