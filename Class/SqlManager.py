from datetime import datetime
#from Class.Tickets import ticket

import pymysql
import pymysql.cursors


class mySqlUtility():
    @staticmethod
    def connection():
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Solobari1',
                                     db='FlightPooling',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        #con = DriverManager.getConnection("jdbc:mysql://localhost:3306/Fantacalcio?autoReconnect=true&useSSL=false",
                                         # "root", "Solobari1");
        return connection
    def updateSQL(self, sqlStatement, sqlArgs):
        #Used to update line in table
        connection = mySqlUtility.connection()


        try:
            with connection.cursor() as cursor:
                 cursor.execute(sqlStatement,sqlArgs)
                 connection.commit()
        except Exception as error:
            print(error)

        finally:
            connection.close()

    def selectSQL(self, sqlStatement, sqlArgs):
        # Used to select line sin table
        connection = mySqlUtility.connection()

        try:
            with connection.cursor() as cursor:
                    cursor.execute(sqlStatement, sqlArgs)
                    queryResult = cursor.fetchall()

        except e:
            print(e)

        finally:
            connection.close()
        return queryResult

class managerSql():
    def saveRun(self,RunDateTimeString,voloCode,voloCodeReturn):

        '''
        Method will update the header table saving the last run
        '''

        voloId = voloCode + "_" + RunDateTimeString.replace(' ', '').replace(':','').replace('/','')
        voloIdReturn = voloCodeReturn + "_" + RunDateTimeString.replace(' ', '').replace(':','').replace('/','')
        RunDateTime = datetime.strptime(RunDateTimeString,'%d/%m/%Y %H:%M:%S')
        IsLastRun="Y"
        sqlStatmentHD = '''insert into POOLING_VOLO_HD (VOLO_ID,VOLOCODE,RunDateTime,IsLast) values (%s,%s,%s,%s)'''
        sqlValues=(voloId,voloCode,RunDateTime ,IsLastRun)
        sqlValuesReturn=(voloIdReturn,voloCodeReturn,RunDateTime ,IsLastRun)
        utility=mySqlUtility
        utility.updateSQL(self,sqlStatmentHD,sqlValues)
        utility.updateSQL(self, sqlStatmentHD, sqlValuesReturn)


    def saveTicket(self,ticket):
        '''Saving the into the body table'''
        voloId = ticket.code + "_" + ticket.dateRunString.replace(' ', '').replace(':', '').replace('/','') + "_" + ticket.departure + "_" + \
                 ticket.depDateTimeString.replace(' ', '').replace(':', '').replace('/', '')
        DepDate = datetime.strptime(ticket.depDateTimeString,'%m/%d/%Y %H:%M')
        ArrDate = datetime.strptime(ticket.arrDateTimeString,'%m/%d/%Y %H:%M')
        voloMatchCode = ticket.code + "_" + ticket.depDateTimeString.replace(' ', '').replace(':', '').replace('/', '') +\
                        ticket.arrDateTimeString.replace(' ', '').replace(':', '').replace('/', '')
        departure = ticket.departure
        dest = ticket.arrival
        price = ticket.price
        ccy = ticket.ccy

        sqlStatmentHD = '''insert into POOLING_VOLO_bD (VOLO_ID,VOLO_MATCH_CODE,DepDate,RetDate,
                                Departure,Destination,Price,currency) values (%s,%s,%s,%s,%s,%s,%s,%s)'''
        sqlValues = (voloId,voloMatchCode,DepDate,ArrDate,departure,dest,price,ccy)
        utility = mySqlUtility
        utility.updateSQL(self, sqlStatmentHD, sqlValues)
