from Class.RunManager import runManager
from Class.Tickets import ticket
import datetime
import time

class runManagerRyan(runManager):
    def parseTickets(self,content):
        '''The method will take as imput the API result from Ryan and return a dictionary with all the
        object tickets inside to be saved'''
        Tickets = {}
        for trip in content['trips']:
            for day in trip['dates']:
                for flight in day['flights']:
                   try:

                       dateRunString = datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y %H:%M:%S')
                       departure = trip['origin']
                       arrival = trip['destination']
                       depDateTimeString = flight['flightKey'].split("~")[5]
                       code = flight['flightKey'].split("~")[0]+ "-" + flight['flightKey'].split("~")[1]
                       arrDateTimeString = flight['flightKey'].split("~")[7]
                       price = flight['regularFare']['fares'][0]['amount']
                       currency = content['currency']
                       Tick = ticket(dateRunString,code,departure,depDateTimeString,arrival,arrDateTimeString,price,currency)
                       voloId = Tick.code + "_" + Tick.dateRunString.replace(' ', '').replace(':', '').replace('/', '') + "_" + Tick.departure + "_" +\
                                Tick.depDateTimeString.replace(' ', '').replace(':', '').replace('/', '')
                       Tickets[voloId] = Tick
                   except Error as e:
                       print(e)

        return Tickets
    def parseRun(self, content):
        '''The method will return a vector to save both the fly home and the return'''
        runParameter = []
        runParameter.append(datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y %H:%M:%S'))
        trip = content['trips'][0]
        tripReturn = content['trips'][1]
        for day in trip['dates']:
            for flight in day['flights']:
                try:
                    runParameter.append(flight['flightKey'].split("~")[0] + "-" + flight['flightKey'].split("~")[1])
                    break
                except Error as e:
                    print (e)
            break
        for day in tripReturn['dates']:
            for flight in day['flights']:
                try:
                    runParameter.append(flight['flightKey'].split("~")[0] + "-" + flight['flightKey'].split("~")[1])
                    break
                except Error as e:
                    print (e)
            break
        return runParameter



'''BVA->BRI
-- 04/22/2019 12:25 - 04/22/2019 14:45 - 141.77 EUR
-- 04/23/2019 12:25 - 04/23/2019 14:45 - 82.61 EUR
-- 04/24/2019 12:25 - 04/24/2019 14:45 - 119.33 EUR
-- 04/25/2019 12:25 - 04/25/2019 14:45 - 141.77 EUR
-- 04/26/2019 12:25 - 04/26/2019 14:45 - 141.77 EUR
BRI->BVA
-- 05/02/2019 09:25 - 05/02/2019 12:00 - 62.41 EUR
-- 05/03/2019 09:25 - 05/03/2019 12:00 - 58.13 EUR
-- 05/04/2019 09:25 - 05/04/2019 12:00 - 119.33 EUR
-- 05/05/2019 09:40 - 05/05/2019 12:15 - 98.93 EUR
-- 05/06/2019 09:25 - 05/06/2019 12:00 - 82.61 EUR
-- 05/07/2019 09:25 - 05/07/2019 12:00 - 52.32 EUR
-- 05/08/2019 09:25 - 05/08/2019 12:00 - 119.33 EUR



            print(trip['origin'] + "->" + trip['destination'])
            for day in trip['dates']:
                for flight in day['flights']:
                    print("-- " + flight['flightKey'].split("~")[5] + " - " + flight['flightKey'].split("~")[7] + " - " + str(flight['regularFare']['fares'][0]['amount']) + " " + content['currency'])'''



