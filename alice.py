globalTimeCount = 0
globalTripPath = ""
cityCount, roadCount, revisitThreshold, maximumDuration, startCity = map(int, input().split())

city_dict = [""]*cityCount
cityDetails = [[0]*3]*cityCount
cityDetails = [[0] * 3 for _ in range(cityCount)]
for x in range(cityCount):
     index, name, visitTime = input().split()
     visitTime = int(visitTime)
     city_dict[x] = name
     cityDetails[x] = [x, visitTime, -1]

roadNetwork = [[-1] * cityCount for _ in range(cityCount)]
for x in range(roadCount):
    citya, cityb, distance = map(int, input().split())
    roadNetwork[citya][cityb] = distance 
    roadNetwork[cityb][citya] = distance

def getNextLocation(presentCity):
    global globalTimeCount
    global roadNetwork
    global cityDetails
    global revisitThreshold

    newDestinations = [x for x in range(cityCount) if roadNetwork[presentCity][x]>0]
    nextlocation = -1
    mindist = float("inf")
    for x in newDestinations:
        # if distance to the new location is less the current lowest dist
        if roadNetwork[presentCity][x] <= mindist:
            # if the new location can be (Re)visited
            if (cityDetails[presentCity][2] + roadNetwork[presentCity][x] - cityDetails[x][2] >= revisitThreshold) or (cityDetails[x][2] == -1):
                #  if the global time limit is not reached after visiting this new city
                if(cityDetails[x][1] + cityDetails[presentCity][2] + roadNetwork[presentCity][x] <= maximumDuration):
                    mindist = roadNetwork[presentCity][x]
                    nextlocation = x
    return nextlocation

currentCity = startCity
prevcity = currentCity
while globalTimeCount < maximumDuration :
    if globalTimeCount == 0 :
        globalTimeCount += cityDetails[currentCity][1]
        globalTripPath += city_dict[currentCity]
        cityDetails[currentCity][2] = globalTimeCount
        currentCity = getNextLocation(presentCity=currentCity)
        continue
    if currentCity >= 0 :
        globalTimeCount += roadNetwork[currentCity][prevcity] + cityDetails[currentCity][1]
        globalTripPath += " " + city_dict[currentCity]
        cityDetails[currentCity][2] = globalTimeCount
        prevcity = currentCity
        currentCity = getNextLocation(presentCity=currentCity)
    else :
        print(globalTripPath)
        print(globalTimeCount)
        break
    

