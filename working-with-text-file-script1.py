import csv
with open('sample_file.txt', 'r') as f:
    # reading the file in a list. splitlines() function is used to splitlines as seperate value in list.
    content = f.read().splitlines()
    # concatenating the list back into a string
    # join fuction is used to join list contents/values. '/n' option is used to insert a new line between each value of list.
    my_str = '\n'.join(content)
    print(my_str)