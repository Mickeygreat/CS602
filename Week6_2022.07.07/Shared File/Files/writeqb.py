# reading a file you want for input
# and printing it out at a separate file

infile = open("qbdata.txt", "r") # the file you want to read
outfile = open("qbnames.txt", "w") # the file you want to write your output

aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[1] + ', ' + items[0]
    outfile.write(dataline + '\n') # new line to write different thing on a separate line
    aline = infile.readline()

infile.close()
outfile.close()
