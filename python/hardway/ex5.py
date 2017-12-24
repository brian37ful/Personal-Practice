name = "Brian"
age = 35
height = 74
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"

print ("Let's talk about %s." % (name))
print ("He's %d inches tall." % (height))
print ("He's %d pounds heavy." % weight)
print ("Actually that's not to heavy/")
print ("His teeth are usually %s." %teeth)

print ("If I add %d, %d and %d. I get %d." \
    % (age, height, weight, age + height + weight))

print ("If I add {0}, {1} and {2}. I get {3}."
    .format(age, height, weight, age + height + weight))

test = [63, {1:4}]
print ("Let's talk about %r." % (test))
print ("Let's talk about %s." % (test))