import requests
import json
from Class.ryanair import flightsRyanair
from Class.RunManagerRyan import runManagerRyan
from Class.SqlManager import mySqlUtility
from Class.SqlManager import managerSql
from datetime import datetime
import time
from Class import company

FLIGHT_URL="https://desktopapps.ryanair.com/en-gb/availability?"
#FLIGHT_URL="https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateIn=" + DATEIN + "&DateOut=" + DATEOUT + "&Destination=" + DESTINATION + "&FlexDaysIn=6&FlexDaysOut=4&INF=0&Origin=" + ORIGIN + "&RoundTrip=true&TEEN=0"

API_URL="https://api.ryanair.com/aggregate/3/common?embedded=airports&market=en-gb"
#API_URL="http://localhost:8080/airports.json"

requests.packages.urllib3.disable_warnings()

## Print flights
def printFlights(origin, destination, datein, dateout, type_of_flight="regularFare"):
    url = FLIGHT_URL + "ADT=1&CHD=0&DateIn=" + datein + "&DateOut=" + dateout + "&Destination=" + destination + "&FlexDaysIn=6&FlexDaysOut=4&INF=0&Origin=" + origin + "&RoundTrip=true&TEEN=0" + "&ToUs=AGREED"
    r = requests.get(url)
    j = json.loads(r.content)

    for trip in j['trips']:
        print (trip['origin'] + "->" + trip['destination'])
        for day in trip['dates']:
             for flight in day['flights']:
                 print ("-- " + flight['flightKey'].split("~")[5] + " - " + flight['flightKey'].split("~")[7] + " - " + str(flight[type_of_flight]['fares'][0]['amount']) + " " + j['currency'])

## Return json airport object with name,seoName and iataCode from string
def searchAirport(searchname):

    r = requests.get(API_URL)
    j = json.loads(r.content)
    for airport in j['airports']:
        if (searchname.lower() in airport['name'].lower()) or (searchname.lower() in airport['seoName'].lower()):
            result = {}
            result['name'] = airport['name']
            result['seoName'] = airport['seoName']
            result['iataCode'] = airport['iataCode']
            return result

def main():
   #result= searchAirport('Bari')
   #print (result)
   #FLIGHT_URL = "https://desktopapps.ryanair.com/en-gb/availability?"
   # FLIGHT_URL="https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateIn=" + DATEIN + "&DateOut=" + DATEOUT + "&Destination=" + DESTINATION + "&FlexDaysIn=6&FlexDaysOut=4&INF=0&Origin=" + ORIGIN + "&RoundTrip=true&TEEN=0"

   #API_URL = "https://api.ryanair.com/aggregate/3/common?embedded=airports&market=en-gb"
   # API_URL="http://localhost:8080/airports.json"
   volo = flightsRyanair()



   ORIGIN = "BVA"
   DESTINATION = "BRI"
   DATEIN = "2019-05-02"
   DATEOUT = "2019-04-22"
   TYPE_OF_FLIGHT = "regularFare"

   biglietti = volo.getFlights(ORIGIN,DESTINATION,DATEIN,DATEOUT)
   m = runManagerRyan()
   runPar = m.parseRun(biglietti)
   tickets = m.parseTickets(biglietti)
   m.saveRun(runPar)
   m.saveTickets(tickets)
   m.getLastTickets()


   #volo.printFlights(biglietti)

   #printFlights(ORIGIN, DESTINATION, DATEIN, DATEOUT, TYPE_OF_FLIGHT)
   #print (p)

'''def TestDB():
    con = mySqlUtility()
    con.connection()
    ts=time.time()
    i=datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
    print(i)
    TestMat=[[i,'FR1234']]
    manager = managerSql()
    manager.insertFlight(TestMat)'''



   # print ("STR_TO_DATE('" + TestMat[0][0] + "','%Y/%m/%d %H:%i%s'),Y)")
if __name__ == "__main__":
    main()