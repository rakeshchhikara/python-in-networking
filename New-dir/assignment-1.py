### YOUR CODE STARTS HERE

word = open('a.txt', 'r')
word.seek(4)
print(word.read(5))

word.close()