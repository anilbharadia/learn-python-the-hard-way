the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes thriugh a list 
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we do not know what is in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = range(0, 6)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# index based access similar to java array
print "A fruit at index 0 is %s" % fruits[0]
print "A fruit at index 1 is %s" % fruits[1]

