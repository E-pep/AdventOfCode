import numpy


# Find the amount of houses with atleast one present
def FindHouses(file):
    TotalHouses = 1
    CurrentPosition = [0, 0]
    ReceivedHousesPositionList = []
    ReceivedHousesPositionList.append([0,0])
    # ReceivedHousesPositionList.append(CurrentPosition)
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
            if [CurrentPosition[0], CurrentPosition[1]] not in ReceivedHousesPositionList:
                print("current position in if:")
                print(CurrentPosition)
                ReceivedHousesPositionList.append([CurrentPosition[0], CurrentPosition[1]])
    print("receivedHousePositions:")
    print(len(ReceivedHousesPositionList))



# part 2 find the amount of houses with help of robo-santa

def FindHousesRoboSanta(file):
    TotalHouses = 1
    CurrentPosition = [0, 0]
    CurrentPositionRobosanta = [0,0]
    ReceivedHousesPositionList = []
    ReceivedHousesPositionList.append([0,0])

    # variable which switches between santa and robosanta
    switch = False
    for line in file:
        for character in line:
            if switch == False:
                if character == '>':
                    CurrentPosition[0] = CurrentPosition[0] + 1
                elif character == '<':
                    CurrentPosition[0] = CurrentPosition[0] - 1
                elif character == '^':
                    CurrentPosition[1] = CurrentPosition[1] + 1
                elif character == 'v':
                    CurrentPosition[1] = CurrentPosition[1] - 1

                if [CurrentPosition[0], CurrentPosition[1]] not in ReceivedHousesPositionList:
                    ReceivedHousesPositionList.append([CurrentPosition[0], CurrentPosition[1]])

            elif switch == True:
                if character == '>':
                    CurrentPositionRobosanta[0] = CurrentPositionRobosanta[0] + 1
                elif character == '<':
                    CurrentPositionRobosanta[0] = CurrentPositionRobosanta[0] - 1
                elif character == '^':
                    CurrentPositionRobosanta[1] = CurrentPositionRobosanta[1] + 1
                elif character == 'v':
                    CurrentPositionRobosanta[1] = CurrentPositionRobosanta[1] - 1
                if [CurrentPositionRobosanta[0], CurrentPositionRobosanta[1]] not in ReceivedHousesPositionList:
                    ReceivedHousesPositionList.append([CurrentPositionRobosanta[0], CurrentPositionRobosanta[1]])
            switch = not switch
    print("receivedHousePositions:")
    print(len(ReceivedHousesPositionList))

if __name__ == "__main__":
    # open input file
    f = open("input.txt", "r")
    # FindHouses(f)
    FindHousesRoboSanta(f)