print("Let's practice everything.")
print("You\'d need to know about escapes with \\ that"
	   "do \n newlines and \t tabs.")

poem = """
\t The lovely world
With logic so firmly planted
cannor dicern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("-----------")
print poem
print("-----------")

five = 10 - 2 + 3 - 6
print("This should be five: {}".format(five))


def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

started_point = 1000
beans, jars, crates = secret_formula(started_point)

print("With a starting point of {}.".format(started_point))
print("We got {} beans, {} jars, {} crates.".format(
	beans, jars, crates))

started_point = started_point / 10
beans, jars, crates = secret_formula(started_point)
print("With a starting point of {}.".format(started_point))
print("We got {} beans, {} jars, {} crates.".format(
	beans, jars, crates))