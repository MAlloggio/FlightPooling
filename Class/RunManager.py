from Class.company import flightsCompany
from Class.SqlManager import managerSql
from Class.Tickets import ticket
import time
import datetime

class runManager():

    def runResearch(self,flightsCompany,destination, datein, dateout):
        content=flightsCompany.getFlights(destination, datein, dateout)
        return content

    def saveRun(self,runParam):
        try:
            manager = managerSql
            dateRunString = runParam[0]
            flightCode = runParam[1]
            flightCodeReturn = runParam[2]
            manager.saveRun(self,dateRunString,flightCode,flightCodeReturn)
        except error as e:
            print(error)

    def saveTickets(self,tickets):
        #tickets is a dictionary so i need to loop into it

        for code in tickets:
            try:
                ticket = tickets[code]
                manager = managerSql
                manager.saveTicket(self,ticket)
            except error as e:
                print(error)

    def getLastTickets(self,runParam):
        try:
            manager = managerSql
            lastSavedTickets = manager.getLastTickets(self,runParam)
        except e as Error:
            print(e)
        '''We're going now to parse the query result to create a dictionary of Tickets'''
        lastTickets = {}
        for element in lastSavedTickets:

            '''self,dateRunString,code,departure,depDateTimeString,arrival,arrDateTimeString,price,ccy'''
            LastTicket = ticket(element['RunDateTime'].strftime('%d/%m/%Y %H:%M:%S'),element['VOLOCODE'],\
                                element['Departure'],element['DepDate'].strftime('%d/%m/%Y %H:%M:%S'), element['Destination'], \
                                element['RetDate'].strftime('%d/%m/%Y %H:%M:%S'),element['Price'],element['currency'])
            voloMatchCode = element['VOLO_MATCH_CODE']
            lastTickets[voloMatchCode] = LastTicket


        '''The method return an array of dictionary. We need to parse in order to take the tickets'''
        return lastTickets


    def changeLastRunTicket(self, runParam):
        try:
            manager = managerSql
            manager.changeLastRunTicket(self,runParam)
        except e as Error:
            print(e)

    def compareTicketPrice(self,tickets,lastTickets):
        '''The method will compare the price of the tickets old vs new and will return a dictionary with the list'''
        cheaperTickets=[]
        for code in tickets:
            ticket = tickets[code]
            voloMatchCode = ticket.code + "_" + ticket.depDateTimeString.replace(' ', '').replace(':', '').replace('/','') + \
                            ticket.arrDateTimeString.replace(' ', '').replace(':', '').replace('/', '')
            if voloMatchCode in lastTickets:
              lastTicket = lastTickets[voloMatchCode]
              if ticket.isCheaper(lastTicket):
                    cheaperTickets.append(ticket)
        return cheaperTickets

   #FR - 8708_050220190925050220191200






