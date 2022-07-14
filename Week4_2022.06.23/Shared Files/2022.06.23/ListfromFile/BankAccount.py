'''
Created on Feb 17, 2020
@author: ruded
'''

import csv


def readData(datafile):
    aList = []
    f = open(datafile)
    for row in csv.reader(f):
        aList.append(row)
    return aList
       
def printAccts(alist):
    for acct in alist:
        print(acct)
        
        
def findAcct(alist, acctNum):
    acctFound = False

    for acct in alist:
        # print(acct[1] + " " + acct[3])
        if acct[1] == acctNum or acct[3] == acctNum:
            acctFound = True
            break
        else:
            acctFound = False
        
    if acctFound: 
        if acctNum == acct[1]:
            print("Checking Account: {}   Name on Account: {}".format(acctNum, acct[0]))
            print("Current Balance: ${:,.2f}".format(eval(acct[2])))
        else:
            print("Savings Account: {}   Name on Account: {}".format(acctNum, acct[0]))
            print("Current Balance: ${:,.2f}".format(eval(acct[4])))
    else:
        print("Account: {} does not exist!".format(acctNum))

        
def creditAcct(alist, acctNum, amount):
    found = False
    for i in alist:
        acctFound = (i[1] == acctNum or i[3] == acctNum)
        if acctFound:
            if i[1] == acctNum:
                i[2] = str(eval(i[2]) + amount)
                print("Checking Account: {}   Name on Account: {}".format(acctNum, i[0]))
                print("Current Balance: ${:,.2f}".format(eval(i[2])))
                found = True
            else:
                i[4] = str(eval(i[4]) + amount)
                print("Savings Account: {}   Name on Account: {}".format(acctNum, i[0]))
                print("Current Balance: ${:,.2f}".format(eval(i[4])))
                found = True
        if found:
            break


def debitAcct(alist, acctNum, amount):
    found = False
    for i in alist:
        acctFound = (i[1] == acctNum or i[3] == acctNum)
        if acctFound:
            if i[1] == acctNum:
                if (eval(i[2]) - amount) >= 0:
                    i[2] = str(eval(i[2]) - amount)
                    print("Checking Account: {}   Name on Account: {}".format(acctNum, i[0]))
                    print("Current Balance: ${:,.2f}".format(eval(i[2])))
                    found = True
                else:
                    print("Error, Not enough funds...")
                    print("Checking Account: {}   Name on Account: {}".format(acctNum, i[0]))
                    print("Current Balance: ${:,.2f}".format(eval(i[2])))
                    found = True
            else:
                if (eval(i[4]) - amount) >= 0:
                    i[4] = str(eval(i[4]) - amount)
                    print("Savings Account: {}   Name on Account: {}".format(acctNum, i[0]))
                    print("Current Balance: ${:,.2f}".format(eval(i[4])))
                    found = True
                else:
                    print("Error, Not enough funds...")
                    print("Savings Account: {}   Name on Account: {}".format(acctNum, i[0]))
                    print("Current Balance: ${:,.2f}".format(eval(i[4])))
                    found = True
        if found:
            break

                   
def main():
    accounts = readData("AccountData.csv")
    printAccts(accounts)
    print()
    
    accountNumber = input("Enter account number: ")
    findAcct(accounts, accountNumber)
    
    accountNumber = input("Enter account number: ")
    depositAmt = eval(input("Enter deposit: "))
    creditAcct(accounts, accountNumber, depositAmt)
    
    accountNumber = input("Enter account number: ")
    withdrawAmt = eval(input("Enter withdraw: "))
    debitAcct(accounts, accountNumber, withdrawAmt)


main()

