#============================================================================
# Exercise using matplotlib to make a simple contour plot on a map.
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
import mpl_toolkits.basemap as bm


#- Reading data for a timeslice, latitude, and longitude:

fileobj = S.NetCDFFile('air.mon.mean.nc', mode='r')
T_time0 = fileobj.variables['air'].getValue()[0,:,:]
T_units = fileobj.variables['air'].units
lon = fileobj.variables['lon'].getValue()
lat = fileobj.variables['lat'].getValue()
fileobj.close()


#- Make 2-D longitude and latitude arrays:

[lon2d, lat2d] = N.meshgrid(lon, lat)


#- Set up map:

mapproj = bm.Basemap(projection='cyl', 
                     llcrnrlat=-90.0, llcrnrlon=0.0,
                     urcrnrlat=90.0, urcrnrlon=360.0)
mapproj.drawcoastlines()
mapproj.drawparallels(N.array([-90, -45, 0, 45, 90]), labels=[1,0,0,0])
mapproj.drawmeridians(N.array([0, 90, 180, 270, 360]), labels=[0,0,0,1])
lonall, latall = mapproj(lon2d, lat2d)


#- Make a contour plot of the temperature:

mymapf = plt.contourf(lonall, latall, T_time0, 10, cmap=plt.cm.Reds)
mymap = plt.contour(lonall, latall, T_time0, 10, colors='k')
plt.clabel(mymap, fontsize=12)
plt.title('Air Temperature [' + T_units + ']')
plt.colorbar(mymapf, orientation='horizontal')


#- Call show and savefig:

plt.savefig('exercise-T-basemap.png')
plt.show()


#===== end file =====
