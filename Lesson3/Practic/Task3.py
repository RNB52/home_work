import sys
filename = sys.argv[0]
f = open(filename, 'r') 
for line in list(f)[: : -1]: 
	print(line)
f.close() 