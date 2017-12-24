ten_things = "a b c d e f g h"

print "There aren't ten things. Let's fix it"

stuff = ten_things.split(' ')
more_things = ['i', 'j', 'k', 'l', 'm']

while len(stuff) is not 10:
	next_one = more_things.pop()
	print ("Add thing {0!s}".format(next_one))
	stuff.append(next_one)
	print ("There are {} stuff here.".format(len(stuff)))

print ("Here we go: {!s}".format(stuff))

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]

print stuff.pop()
print stuff

print "*".join(stuff)