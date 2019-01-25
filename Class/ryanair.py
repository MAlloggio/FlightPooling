from Class.company import flightsCompany

class flightsRyanair(flightsCompany):

    def getFlights(self,origin, destination, datein, dateout, type_of_flight="regularFare"):
        APIreq= self.API_FLIGHT + "ADT=1&CHD=0&DateIn=" + datein + "&DateOut=" + dateout + "&Destination=" + destination + "&FlexDaysIn=6&FlexDaysOut=4&INF=0&Origin=" + origin + "&RoundTrip=true&TEEN=0" + "&ToUs=AGREED"
        content = super().GetFlight(APIreq)
        return content

    def printFlights(self,content):
        for trip in content['trips']:
            print(trip['origin'] + "->" + trip['destination'])
            for day in trip['dates']:
                for flight in day['flights']:
                    print("-- " + flight['flightKey'].split("~")[5] + " - " + flight['flightKey'].split("~")[7] + " - " + str(flight['regularFare']['fares'][0]['amount']) + " " + content['currency'])

