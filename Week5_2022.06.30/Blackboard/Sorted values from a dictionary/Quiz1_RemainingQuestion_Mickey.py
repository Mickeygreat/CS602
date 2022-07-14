def main():

    puzzle = "python is a snake"

    result1 = bonus_round(puzzle)
    lucky2 = "cdmna"
    result2 = bonus_round(puzzle, lucky2)
    print(f"Original Puzzle:             {puzzle}")
    print(f"Dashes with default letters: {result1}")
    print(f"Dashes with letters {lucky2}:   {result2}")

def bonus_round(puzzle, y =" "):
    # x = "python is a snake"
    seperate = list(puzzle)
    # y = "cdmna" #maybe call y
    i = 0

    default_letters = "tnse"
    default = ""

    for letter in puzzle:
        if letter in default_letters:
          default += seperate[i]
          i+=1

        elif letter not in default_letters and letter != " ":
          default += "-"
          i+=1

        else:
          default += " "
          i+=1
    # return default

    a = 0
    sentence = ""
    for letter in puzzle:

        if letter in y:
          sentence = sentence + seperate[a]
          a+=1
        elif letter not in y and letter != " ":
          sentence = sentence + "-"
          a+=1
        else:
          sentence = sentence + " "
          a+=1

    # return sentence
    a = [default, sentence]
    return a[0], a[1]




main()
