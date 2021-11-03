from constants import orbits,vehicles,weathers

weather,orbitOneSpeed,orbitTwoSpeed = None,None,None
# taking input from file
import sys
with open(sys.argv[1]) as f:
    weather,orbitOneSpeed,orbitTwoSpeed = f.readline().split()

cratersIncreaseBy = weathers[weather.lower()]['cratersIncreaseBy']
#assign speeds to each orbit
orbits[1]['orbitSpeed'],orbits[2]['orbitSpeed']= int(orbitOneSpeed),int(orbitTwoSpeed)

# Calculate the number of craters
orbits[1]['noOfCraters'] += int(orbits[1]['noOfCraters'] * cratersIncreaseBy/100)
orbits[2]['noOfCraters'] += int(orbits[2]['noOfCraters'] * cratersIncreaseBy/100)

# result format
result = {'vehicle' : None,'orbit' : None}

# assuming min time taken as maximum
minTimeTaken = float("inf")

# function to find time taken for each vehicle for all orbits
def getTimeTaken(vehicle):
    global minTimeTaken
    timeTaken = float("inf")
    # for each orbit
    for orbit in orbits:
        # measing the attributes
        distance = orbits[orbit]['distance']
        orbitSpeed = min(orbits[orbit]['orbitSpeed'],vehicles[vehicle]['speed'])
        time = distance/orbitSpeed
        noOfCraters = orbits[orbit]['noOfCraters']
        timeToCrossAllCraters = vehicles[vehicle]['timeToCrossCrater'] * noOfCraters
        timeTaken = min(timeTaken,time + timeToCrossAllCraters)
        # comparing with minTimeTaken
        if minTimeTaken > timeTaken:
            result['vehicle'] = vehicle
            result['orbit'] = orbit
            minTimeTaken = timeTaken
    # return the time taken
    return timeTaken

# calculating time for each vehicle
for vehicle in vehicles:
    timeTaken = getTimeTaken(vehicle)

# reformatting the output
if result['vehicle'] == 'superCar':
    result['vehicle'] = 'car'
if result['orbit']==1:
    result['orbit'] = 'orbit1'
else:
    result['orbit'] = 'orbit2'

# printing the output
print(result['vehicle'].upper(),result['orbit'].upper())