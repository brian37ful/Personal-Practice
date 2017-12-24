from sys import argv


if len(argv) is 1:
	print "Need your name!!"
	exit(1)

script, user_name = argv
prompt = "> "

print "Hi {0}, I'm the {1} script.".format(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me {}?".format(user_name)

like = raw_input(prompt)

print "Where do you live {}?".format(user_name)
lives = raw_input(prompt)

print "What kind of computer do you have {}?".format(user_name)
computer = raw_input(prompt)

print """
Alright, so you said {0!r} about liking me.
You live in {1!r}. Not sure where that is.
And you have a {2!r} computer. Nice!!
""".format(like, lives, computer)