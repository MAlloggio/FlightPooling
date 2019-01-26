import requests
import json

requests.packages.urllib3.disable_warnings()

class flightsCompany():
    def __init__(self,API_FLIGHT, API_AIRPORT):
        self.API_FLIGHT = API_FLIGHT
        self.API_AIRPORT = API_AIRPORT

    def GetFlight (self,APIreq):
        req = requests.get(APIreq)
        content = json.loads(req.content)
        return content

    def getFlights (self,origin, destination, datein, dateout, type_of_flight="regularFare"):
        '''method to be overloaded in the dedicated class'''
        return ""
    def getFlightCode(self,content):
        FlightCode=""
        return FlightCode








