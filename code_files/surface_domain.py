#============================================================================
# An example of a surface domain class.
#
# Author: Johnny Lin. 
#
# Copyright (c) 2006-2011 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#============================================================================


#- Module imports:

import numpy as N


#- Define the class:

class SurfaceDomain(object):
    def __init__(self, lon, lat):
        self.lon = N.array(lon)   #- Guarantee lon is a NumPy array
        self.lat = N.array(lat)   #- Guarantee lat is a NumPy array

        shape2d = (N.size(self.lat), N.size(self.lon))
        self._lonall = N.zeros(shape2d, dtype='f')
        self._latall = N.zeros(shape2d, dtype='f')
        for i in xrange(shape2d[0]):
            for j in xrange(shape2d[1]):
                self._lonall[i,j] = self.lon[j]
                self._latall[i,j] = self.lat[i]

        #[xall, yall] = N.meshgrid(self.lon, self.lat)
        #self._lonall = xall
        #self._latall = yall
        #del xall, yall


#- Create example instance:

domain01 = SurfaceDomain(range(5), range(4))


#- Print some diagnostics:

if __name__ == '__main__':
    print "Longitude vector:  ", domain01.lon
    print "Latitude vector:  ", domain01.lat
    print "Longitude (2-D grid):  \n", domain01._lonall
    print "Latitude (2-D grid):  \n", domain01._latall


#===== end file =====
