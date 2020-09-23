# importing regex
import re

def FindNiceStrings(file):
    result = 0
    for line in file:
        print("line:"+ line)

        # count the vowels aeiou
        vowels = line.count("a") + line.count("e") + line.count("i") + line.count("o")  + line.count("u")
        if vowels < 3:
            continue

        # check on double letters
        doubleLetters = [len(sub.group()) for sub in re.finditer(r'((\w)\2)+', line)]
        if doubleLetters == []:
            continue

        # check if not contains ab, cd, pq,xy
        abcd = line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy")
        print("size" + str(abcd))
        if abcd > 0:
            continue

        print('nice')
        result = result + 1

    print(result)

def FindNiceStrings2(file):


if __name__ == "__main__":
    # open input file
    f = open("input.txt", "r")
    FindNiceStrings2(f)