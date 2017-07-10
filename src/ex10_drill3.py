# -*- coding: utf-8 -*-

import sys

print "sys.stdout.encoding = ", sys.stdout.encoding
#sys.stdout.encoding = 'utf-8' # results in error
#print "sys.stdout.encoding = ", sys.stdout.encoding

print "\a" # sound bell
print '\\'
print '\''
print '\"'
print 'a\bb' # backspace
print '\f' # form feed -> https://stackoverflow.com/a/3098328
print 'a\nb'
print 'a\N{name}b' # TODO find on google
print 'abc\rxyz'
print 'abc\rxyz\rrst'

#print u'\u2713'
#print U"\U50000000"
#print u'\U0001F47E'

print '\v'
