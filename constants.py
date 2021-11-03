
#declaring orbits
orbits = {
    1 : {'distance' : 18,'noOfCraters' : 20,'orbitSpeed' : None},
    2 : {'distance' : 20,'noOfCraters' : 10,'orbitSpeed' : None},
}

#declaring vehicles
vehicles = {
    'bike' : {
        'speed' : 10,
         'timeToCrossCrater' : 1/30,
         'requiredWeatherCondition' : {
             'Sunny',
             'Windy'
        }
    },
    'tuktuk' : {
        'speed' : 12,
        'timeToCrossCrater' : 1/60,
        'requiredWeatherCondition' : {
            'Sunny',
            'Rainy'
        }
    },

    'superCar':{
        'speed' : 20,
        'timeToCrossCrater' : 1/20,
        'requiredWeatherCondition' : {
            'Sunny',
            'Rainy',
            'Windy'
        }
    }
}

#declaring weathers
weathers = {
    'sunny' : {
        'cratersIncreaseBy' : -10,
    },
    'rainy' : {
        'cratersIncreaseBy' : 20,
    },
    'windy' : {
        'cratersIncreaseBy' : 0,
    },
}