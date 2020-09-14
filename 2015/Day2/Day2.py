import numpy


def FindWrappingpaper(file):
    result = 0
    for line in file:
        print("line:"+ line)
# split the dimensions and put them in an array (as strings)
        dimensions = line.strip().split(sep="x")
        print(dimensions)
# calculate the formula: 2*l*w + 2*w*h + 2*h*l
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        formula = 2*l*w + 2*w*h + 2*h*l + min([l*w,w*h,h*l])
        result = result + formula
    print("total:" + str(result))


def FindRibbonSize(file):
    result = 0
    for line in file:
        print("line:" + line)
        # split the dimensions and put them in an array (as strings)
        dimensions = line.strip().split(sep="x")
        print(dimensions)
        # calculate the formula: find smallest and second smallest times 2 + the volume
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        # make an ordered list
        list = [l, w, h]
        list.sort()
        print(list)
        smallest = int(list[0])
        secondSmallest = int(list[1])
        print("smallest:"+ str(smallest))
        print("secondsmallest" + str(secondSmallest))
        formula =  (2 * smallest) + (2 * secondSmallest) + l*w*h
        result = result + formula
        print("ribbon per:" + str(formula))
    print("total:" + str(result))
if __name__ == "__main__":
    # open input file
    f = open("input.txt", "r")
    FindRibbonSize(f)