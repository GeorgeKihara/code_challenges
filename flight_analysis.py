

flightsToFrankfurtCount = 0
flightWithMostPassengers = "The file is empty!"
firstFlightWithPassengersLess100 = "There is no flight with passengers less than 100."
airlineWithMostPassengers = "The file is empty!"

def flightAnalysis():
    try:
        # declare the above variables as global
        global flightsToFrankfurtCount, flightWithMostPassengeers, firstFlightWithPassengersLess100, airlineWithMostPassengers

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

        flightWithMostPassengersCount = 0
        foundFirstFlightLess100 = False
        airlineArr = []
        uniqueAirlineArr = []
        airlineWithMostPassengersCount = 0

        for item in allFlights:
            airline = item["airline"]
            destination = item["destination"]
            passengers = item["passengers"]
            # get all flights to Frankfurt
            if destination == "Frankfurt":
                flightsToFrankfurtCount += 1

            # flight with the most passengers
            if passengers > flightWithMostPassengersCount:
                flightWithMostPassengers = airline + " " + destination + " " + str(passengers)
                flightWithMostPassengersCount = passengers 

            # flight with passengers less than 100
            if not foundFirstFlightLess100:
                if passengers < 100:
                    firstFlightWithPassengersLess100 = airline + " " + destination + " " + str(passengers)
                    foundFirstFlightLess100 = True

            # add airline to its own list
            if airline not in uniqueAirlineArr:
                airlineArr.append(
                    {
                        "airline": airline,
                        "passengers": passengers
                    }
                )
                uniqueAirlineArr.append(airline)
            else:
                for i in airlineArr:
                    if (i["airline"] == airline):
                        i["passengers"] += passengers
                        break

        # find airline with the most total number of passengers
        for airline in airlineArr:
            passengers = airline["passengers"]
            if passengers > airlineWithMostPassengersCount:
                airlineWithMostPassengers = airline["airline"] + " " + str(passengers)
                airlineWithMostPassengersCount = passengers

        printOutput()

    except Exception as e:
        raise e
        printOutput()

def printOutput():
    print (flightsToFrankfurtCount)
    print (flightWithMostPassengers)
    print (firstFlightWithPassengersLess100)
    print (airlineWithMostPassengers)

flightAnalysis()