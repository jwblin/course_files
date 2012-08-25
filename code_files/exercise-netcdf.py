#============================================================================
# Exercise to read and write a netCDF file, using an NCEP Reanalysis 1 
# netCDF file for reading.
#
# Author: Johnny Lin. 
#
# Copyright (c) 2006-2012 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#============================================================================


#- Module imports:

import numpy as N
import Scientific.IO.NetCDF as S


#- Reading in the time values:

fileobj = S.NetCDFFile('air.mon.mean.nc', mode='r')
time_data = fileobj.variables['time'].getValue()
time_units = fileobj.variables['time'].units
fileobj.close()


#- Subtract the maximum of the data from the time values:

time_data = time_data - N.min(time_data)
time_units = 'hours'


#- Write out the values to a new file:

fileobj = S.NetCDFFile('newtime.nc', mode='w')
fileobj.createDimension('time', N.size(time_data))
time_var = fileobj.createVariable('time', 'd', ('time',))
time_var.units = time_units
time_var[:] = time_data[:]
fileobj.title = "New netCDF file for the time dimension"
fileobj.close()


#===== end file =====
