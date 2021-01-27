def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-n:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        return my_str


#t = tail('sample_file.txt', 3)
#print(t)

new = tail('configuration.txt', 2)
print(new)