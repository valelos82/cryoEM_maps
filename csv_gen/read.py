f = open('example.txt', 'r')
To get everything in the file, just use read()

file_contents = f.read()
And to print the contents, just do:

print (file_contents)
Don't forget to close the file when you're done.

f.close()
