from sys import argv

script, filename = argv

print "We're going to erase {!r}".format(filename)
print "If you don't want that, hit ctrl-c."
print "If you do want that, hit return."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
# truncate(<n>)
# Delete <n> character from the begin of file.
# If there is no args, means all character.
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("{0!s}\n{1!s}\n{2!s}".format(line1, line2, line3))

print "And finally, we close it."
target.close()

print "Going to check the file we write..."
target = open(filename, "r")

print "Here is the content :"
print target.read()