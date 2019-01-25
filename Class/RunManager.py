from Class.company import flightsCompany
from Class.SqlManager import managerSql

class runManager():

    def runResearch(self,flightsCompany,destination, datein, dateout):
        content=flightsCompany.getFlights(destination, datein, dateout)
        return content

    def saveRun(self,dateRunString,flightCode):
        try:
            manager = managerSql
            manager.saveRun(dateRunString,flightCode)
        except error as e:
            print(error)

    def saveTickets(self,tickets):
        for ticket in tickets:
            try:
                manager = managerSql
                manager.saveTicket(ticket)
            except error as e:
                print(error)


