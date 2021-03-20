from sys import argv
from os.path import exists

script, from_file, to_file = argv


# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()


out_file = open(to_file, 'w')
out_file.write(indata)

print("............Done.")

out_file.close()
in_file.close()