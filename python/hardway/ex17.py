from sys import argv
from os.path import exists

script, src_file, des_file = argv

print ("Copying from {0} to {1}".format(src_file, des_file))

input_data = open(src_file).read()

print ("Input data is {} byte long".format(len(input_data)))

print ("Does the output file exist ? {!r}".format(exists(des_file)))

print ("Ready, hit RETURN to continue, CTRL-C to abort.")

raw_input()

open(des_file, "w").write(input_data)

print ("Alright, all done.")