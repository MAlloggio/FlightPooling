from SqlManager import managerSql

class ticket():
    def __init__(self,dateRunString,code,departure,depDateTimeString,arrival,arrDateTimeString,price,ccy):
        self.dateRunString = dateRunString
        self.code = code
        self.departure = departure
        self.depDateTimeString = depDateTimeString
        self.arrival = arrival
        self.arrDateTimeString = arrDateTimeString
        self.price = price
        self.ccy = ccy

    def isCheaper(self,ticketBench):
        '''boolean to check if a ticket is less expensive that the benchmark one'''
        cheaper = False
        if (self.price < ticketBench.price):
            cheaper = True
        return cheaper














