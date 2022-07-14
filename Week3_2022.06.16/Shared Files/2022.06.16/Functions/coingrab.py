"""


"""
import random

def pick_coin():
    number = random.randint(1,3)
    if number == 1:
        coin = 1
    elif number == 2:
        coin = 5
    else:
        coin = 10
    return coin

def pick_two():
    coin1 = pick_coin()
    coin2 = pick_coin()
    return coin1 + coin2

def main():
    t2 = t3 = t4 = t5 = t6 = 0
    for i in range(1000):
        result = pick_two()
        if result == 2:
            t2 += 1
        elif result == 6:
            t3 += 1
        elif result == 11:
            t4 += 1
        elif result == 15:
            t5 += 1
        else:
            t6 +=1
    print("At end of the game:")
    print(f"Total =  2: {t2}\t Total =  6: {t3}")
    print(f"Total = 11: {t4}\t Total = 15: {t5}\t Total = 20: {t6}")



main()
