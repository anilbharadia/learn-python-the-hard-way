from sys import argv

script, filename = argv

txt = open(filename) # opens a file -> txt

print "Here's your file %r:" % filename

print txt.read() # read file named txt

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
