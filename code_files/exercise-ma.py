#============================================================================
# Exercise of making masked arrays from data in a NCEP Reanalysis 1 netCDF 
# file.
#
# Author: Johnny Lin. 
#
# Copyright (c) 2006-2012 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#============================================================================


#- Module imports:

import numpy as N
import numpy.ma as MA
import Scientific.IO.NetCDF as S


#- Reading example:

fileobj = S.NetCDFFile('air.mon.mean.nc', mode='r')
data = fileobj.variables['air'].getValue()[0,:,:]
lat = fileobj.variables['lat'].getValue()
lon = fileobj.variables['lon'].getValue()
fileobj.close()


#- Make masked and convert to K:

[lonall, latall] = N.meshgrid(lon, lat)
ma_data = MA.masked_where(N.logical_or(latall>45,latall<-45), data)
ma_data = ma_data + 273.15


#- Check poles and equator:

print 'North pole:  ', ma_data[0,:]    #- Should all be masked
print 'South pole:  ', ma_data[-1,:]   #- Should all be masked
print 'Equator:  ', ma_data[36,:]      #- Should all not be masked and in K


#===== end file =====
