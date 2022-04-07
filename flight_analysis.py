

flightsToFrankfurtCount = 0
flightWithMostPassengeers = "The file is empty!"
firstFlightWithPassengersLess100 = "There is no flight with passengers less than 100."
flightWithMostPassengers = "The file is empty!"

def flightAnalysis():
    try:
        # declare the above variables as global
        global flightsToFrankfurtCount, flightWithMostPassengeers, firstFlightWithPassengersLess100, flightWithMostPassengers
        # read data from the input file
        flightFile = open("input.txt","r")
        allFlights = []
        for line in flightFile:
            # add each line as a tuple
            flight = line.split()
            if len(flight) == 3:
                allFlights.append (
                    {
                        "airline" : flight[0],
                        "destination" : flight[1],
                        "passengers" : int(flight[2])
                    }
                )
                
        if (len(allFlights) < 1):
            printOutput()
            return

        # get all flights to Frankfurt
        for item in allFlights:
            print ("item",item)
            if item['destination'] == "Frankfurt":
                flightsToFrankfurtCount += 1

        printOutput()

    except Exception as e:
        raise e
        printOutput()

def printOutput():
    print (flightsToFrankfurtCount)
    print (flightWithMostPassengeers)
    print (firstFlightWithPassengersLess100)
    print (flightWithMostPassengers)

flightAnalysis()