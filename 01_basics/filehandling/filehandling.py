# file handling in python
#file handling in python allows you to read from and write to files. This is important when you want to store data permanently


# Read from a file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# readng one line at a time

file = open('example.txt','r')
line = file.readline()
print(line)
file.close()

# write to a file
file = open('example.txt2','w')
file.write("\nThis is a new added line")
file.close()


#append to a file
file = open('example.txt','a')
file.write("\nThis is a new append line")
file.close()



