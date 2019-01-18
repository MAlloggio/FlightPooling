# Ryanair Python Lib

Simple tests to retrive Ryanair flights

Functions:
* **printFlights**(origin, destination, datein, dateout, type_of_flight="regularFare")
* **searchAirport**(searchname)

Example:
```
./checker_example.py brindisi


  {'seoName': u'brindisi', 'iataCode': u'BDS', 'name': u'Brindisi'}

  BDS->CRL
  -- 02/03/2017 13:35 - 02/03/2017 16:10 - 19.6 EUR
  CRL->BDS
  -- 02/06/2017 10:40 - 02/06/2017 13:10 - 19.6 EUR
  -- 02/10/2017 10:40 - 02/10/2017 13:10 - 19.6 EUR

```
