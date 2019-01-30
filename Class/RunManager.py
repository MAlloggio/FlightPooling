from Class.company import flightsCompany
from Class.SqlManager import managerSql

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
            lastTickets = manager.getLastTickets(self,runParam)
        except e as Error:
            print(e)

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








