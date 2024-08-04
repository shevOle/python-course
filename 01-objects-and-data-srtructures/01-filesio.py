my_file = open('test.txt')

# sets reader cursor to the end of the file
print('read file content', '->', my_file.read())
print()

# nothing is printed, the reader's cursor is in the end of the file already
print('read, cursor at the end of the file', '->', my_file.read())
print()

# reset reader's cursor
my_file.seek(0)
print('read, cursor is reseted', '->', my_file.read())
print()

my_file.seek(0)
print('read lines', '->', my_file.readlines())
print()

# need to close the file to avoid possible filesystem errors
my_file.close()


with open('test.txt') as the_same_file:
    content = the_same_file.read()

print('content after with ... as ...', '->', content)
print()

created_file = open('new_file.txt', 'w')
some_text = 'this is the text created in a script\nit should be written to the newly created file\nas a result of a script run'
created_file.write(some_text)
created_file.close()

read_created_file = open('new_file.txt')
print('newly  created file\'s content', '->', read_created_file.read())
read_created_file.close()
print()

read_created_file = open('new_file.txt', 'a')
new_text = 'some text that should be added in the end'
read_created_file.write(new_text)
read_created_file.close()

with open('new_file.txt') as read_created_file:
    print('created file with appended text', '->', read_created_file.read())

# clear the new_file.txt
with open('new_file.txt', 'w') as f:
    f.write('')

# reset test.txt file
with open('test.txt', 'w') as f:
    f.write(content)