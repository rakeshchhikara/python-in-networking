###############################
##Working with Files in Python
##############################

## Opens a file named a.txt and returns a file object called f
## a.txt it's in the same directory with the python script
## use a correct relative or absolute path
f = open('a.txt', 'r')  # it will be opened in read-only mode

content = f.read()  # reads the entire file as a string
print(content)

f.closed  # => False, file is not closed

## Closes the file
f.close()

## Opens the file in read-only mode and reads its contents in a list
## the file object will be automatically closed
with open('a.txt', 'r') as my_file:
    content = my_file.readlines()  # content is a list

my_file.closed  # => True, my_file has been closed automatically

## file object is an iterable object
with open('a.txt', 'r') as my_file:
    for line in my_file:  # iterating over the lines within the file
        print(line, end='')

## Opens the file in write-mode.
## Creates the file if it doesn't exist or overwrites the file if it already exists
with open('my_file.txt', 'w') as file:
    file.write('This file will be overwritten!')

## Opens the file in append-mode.
## Creates the file if it doesn't exist or appends to its end if it exists
with open('another_file.txt', 'a') as file:
    file.write('Appending to the end!')

## Opens the file for both read and write
## Doesn't create the file if it doesn't exist
with open('my_file.txt', 'r+') as file:
    file.seek(0)  # the cursor is positioned at the beginning of the file
    file.write('Writing and the beginning')  # writing and the beginning

    file.seek(5)  # moving the cursor at position 5
    content = file.read(10)  # reading 10 characters starting from position 5
    print(content)