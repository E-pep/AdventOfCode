import numpy


# Find the amount of houses with atleast one present
def FindHouses(file):
    TotalHouses = 1
    CurrentPosition = [0,0]
    ReceivedHousesPositionList = []
    ReceivedHousesPositionList.append(CurrentPosition)
    for line in file:
        for character in line:
            if character == '>':
                CurrentPosition[0] = CurrentPosition[0] + 1
            elif character == '<':
                CurrentPosition[0] = CurrentPosition[0] - 1
            elif character == '^':
                CurrentPosition[1] = CurrentPosition[1] + 1
            elif character == 'v':
                CurrentPosition[1] = CurrentPosition[1] - 1
            print("current position:")
            print(CurrentPosition)
            if CurrentPosition not in ReceivedHousesPositionList:
                ReceivedHousesPositionList.append(CurrentPosition)
    print("receivedHousePositions:")
    print(ReceivedHousesPositionList)

if __name__ == "__main__":
    # open input file
    f = open("input.txt", "r")
    FindHouses(f)