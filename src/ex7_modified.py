print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end9 + end10 + end11 + end12

print end1, end2, end3, end4, end5, end6,
print end7, end9, end10, end11, end12


print "------------------"

print "this is", 10
print "this is%d" % 10
x = "this is%r"
print x % 20
print "this is %s" % 10
# error # print "this is %d" % "10"
