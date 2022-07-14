"""
Caculate mean, median, mode, and std deviation using the statistics library
"""

import statistics
# documenation at https://docs.python.org/3/library/statistics.html#module-statistics



fileName = input("Enter the file name: ")
f = open(fileName, 'r')

# Input the text, convert it to numbers, and
# add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

f.close()

theMean = statistics.mean(numbers)
theMedian= statistics.median(numbers)
theMode = statistics.mode(numbers)
theStdDev = statistics.stdev(numbers)

print(f"Mean:\t\t{theMean:0.4f}")
print(f"Median:\t\t{theMedian:0.4f}")
print(f"Mode:\t\t{theMode:0.4f}")
print(f"StdDev:\t\t{theStdDev:0.4f}")


