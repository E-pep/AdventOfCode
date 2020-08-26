import numpy


# Part 1
def FindLevel(file):
    level = 0
    for line in file:
        for character in line:
            if character == '(':
                level = level +1
            elif character == ')':
                level = level - 1
    print("level: {}".format(level))


# Part 2
def FindFirstBasement(file):
    counter = 0
    level = 0
    for line in file:
        for character in line:
            counter = counter + 1
            if character == '(':
                level = level +1
            elif character == ')':
                level = level - 1

            if level == -1:
                print("basement reached at: {}".format(counter))
    print("level: {}".format(level))



if __name__ == "__main__":
    # open input file
    f = open("input.txt", "r")
    FindFirstBasement(f)