# good ways to read files from file and print it out
# works good with data files

# method 1

qbfile = open("qbdata.txt", "r") # "r" means read line

for aline in qbfile:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

qbfile.close()
print()

# method 2  - read a line at a time

infile = open("qbdata.txt", "r") # "r" means read line
line = infile.readline()
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
    line = infile.readline()

infile.close()
