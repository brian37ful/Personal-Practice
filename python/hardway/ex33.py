def show_seq_from_zero(the_end, interval):

	i = 0
	numbers = []

	while i < the_end:
		print "At the top i is {}".format(i)
		numbers.append(i)

		i = i + interval
		print ("Numbers now: ", numbers)
		print ("At tje bottom i is {}".format(i))

	print "The numbers: "
	for num in numbers:
		print num

show_seq_from_zero(20, 2)