from sys import argv

filename = raw_input("Enter filename: ")

txt = open(filename) # opens a file identified by given filename and the file object is assigned to txt variable

print "Here's your file %r:" % filename

print "mode = %r" % txt.mode
print "errors = %r" % txt.errors
print "closed = %r" % txt.closed

print txt.read() # call the read method of the file object

txt.close()

print "closed = %r" % txt.closed

print "Lets read again after closing"
print txt.read() # expect error at this line
