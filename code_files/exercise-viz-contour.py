#============================================================================
# Exercise using matplotlib to make a simple contour plot.
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

import numpy as N
import Scientific.IO.NetCDF as S
import matplotlib.pyplot as plt


#- Reading data for a timeslice, latitude, and longitude:

fileobj = S.NetCDFFile('air.mon.mean.nc', mode='r')
T_time0 = fileobj.variables['air'].getValue()[0,:,:]
T_units = fileobj.variables['air'].units
lon = fileobj.variables['lon'].getValue()
lon_units = fileobj.variables['lon'].units
lat = fileobj.variables['lat'].getValue()
lat_units = fileobj.variables['lat'].units
fileobj.close()


#- Make 2-D longitude and latitude arrays:

[lonall, latall] = N.meshgrid(lon, lat)


#- Make a contour plot of the temperature:

mymapf = plt.contourf(lonall, latall, T_time0, 10, cmap=plt.cm.Reds)
mymap = plt.contour(lonall, latall, T_time0, 10, colors='k')
plt.clabel(mymap, fontsize=12)
plt.axis([0, 360, -90, 90])
plt.xlabel('Longitude [' + lon_units + ']')
plt.ylabel('Latitude [' + lat_units + ']')
plt.colorbar(mymapf, orientation='horizontal')


#- Call show and savefig:

plt.savefig('exercise-T-contour.png')
plt.show()


#===== end file =====
