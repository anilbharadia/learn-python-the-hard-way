from sys import argv

script, filename = argv

txt = open(filename) # opens a file identified by given filename and the file object is assigned to txt variable

print "Here's your file %r:" % filename

print txt.read() # call the read method of the file object

print "Type the filename again:"
file_again = raw_input("> ") # just read input from console

txt_again = open(file_again)

print txt_again.read()
