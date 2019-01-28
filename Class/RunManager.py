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




