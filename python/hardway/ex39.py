# Create a mapping of state to abbreviation

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
}


#Create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print ("{!s}".format('-' * 10))
print "NY states has: ", cities['NY']
print "OR states has: ", cities['OR']


# print some states
print ("{!s}".format('-' * 10))
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

#print every states abbreviation
print ("{!s}".format('-' * 10))
for abbrev, city in cities.items():
	print ("{!s} has the city {!s}".format(abbrev, city))

