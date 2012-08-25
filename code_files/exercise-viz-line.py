#============================================================================
# An exercise using matplotlib to make a simple line plot.
#
# Author: Johnny Lin. 
#
# Examples created with help from the matplotlib documentation (though the
# examples themselves are not the documentation's examples).
#
# Copyright (c) 2006-2012 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#============================================================================


#- Module imports:

import Scientific.IO.NetCDF as S
import matplotlib.pyplot as plt


#- Reading data for a point in the Arctic and the time array:

fileobj = S.NetCDFFile('air.mon.mean.nc', mode='r')
T_arctic = fileobj.variables['air'].getValue()[0:100,0,0]
T_units = fileobj.variables['air'].units
time = fileobj.variables['time'].getValue()[0:100]
time_units = fileobj.variables['time'].units
fileobj.close()


#- Make a timeseries plot of the temperature:

plt.plot(time, T_arctic)
plt.xlabel('Time [' + time_units + ']')
plt.ylabel('Temperature [' + T_units + ']')


#- Call show and savefig:

plt.savefig('exercise-T-line.png')
plt.show()


#===== end file =====
