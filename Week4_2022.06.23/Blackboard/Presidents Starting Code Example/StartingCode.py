'''
Created on Oct 7, 2019
'''
import csv

def readData(datafile, pList):
    f=open(datafile)
    for row in csv.reader(f):
        pList.append(row)
 
def printResults(lw, bw, tw, sw):
    print('\nResults' + '\n=====================================')
    print('President(s) >= {} pounds:'.format(lw) + '\n--------------------------------------')
    for p in range(0,len(bw)):
        print('{0} {1} lbs.'.format(bw[p][1], bw[p][3]))
    print('\nPresident(s) <= {} pounds:'.format(tw) + '\n---------------------------------------')
    for p in range(0,len(sw)):
        print('{0} {1} lbs.'.format(sw[p][1], sw[p][3]))
        
        
        
    '''print('\nPresident(s) > {} inches in height:'.format(th) + '\n-------------------------------')
    for p in range(0,len(tl)-1,2):
        print('{0} {1} ins.'.format(n[tl[p]], tl[p+1]))
    print('\nPresident(s) < {} inches in height:'.format(sh) + '\n-------------------------------')
    for p in range(0,len(st)-1,2):
        print('{0} {1} ins.'.format(n[st[p]], st[p+1])) 
    '''
        
def main():
    presidents = []
    readData("president_heights_weights.csv", presidents)
    print(presidents)
    largestWeight = eval(input('Enter largest weight in pounds: '))
    smallestWeight = eval(input('Enter smallest weight: '))  
    '''tallestHeight = eval(input('Enter tallest height in inches: '))  
    shortestHeight = eval(input('Enter shortest height in inches: '))'''
    bigWeights = list()
    smallWeights = list()
    for p in range(0,len(presidents)):
        if eval(presidents[p][3]) >= largestWeight:
            bigWeights.append(presidents[p])
        if eval(presidents[p][3]) <= smallestWeight:
            smallWeights.append(presidents[p])
            
    printResults(largestWeight,bigWeights,smallestWeight,smallWeights)

main()
