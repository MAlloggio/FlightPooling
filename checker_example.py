#!/usr/bin/env python

import sys
from Class.ryanairlib import *

## Fosdem destination :D
ORIGIN="BDS"
DESTINATION="CRL"
DATEIN="2017-02-04"
DATEOUT="2017-02-01"
TYPE_OF_FLIGHT="regularFare"    # choises: regularFare, businessFare, leisureFare

print (searchAirport(sys.argv[1]))
print
printFlights(ORIGIN, DESTINATION, DATEIN, DATEOUT, TYPE_OF_FLIGHT)

