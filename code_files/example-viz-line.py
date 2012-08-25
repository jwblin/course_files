#============================================================================
# Examples of using matplotlib to make line plots and contour plots.
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


#- Make a simple plot:

plt.figure(1)
plt.plot([1, 2, 3, 4], [1, 2.1, 1.8, 4.3])
plt.axis([0, 8, -2, 7])
plt.xlabel('Automatic Range')
plt.ylabel('Made-up Numbers')


#- Make a little more complex plot:

plt.figure(2)
plt.plot([1, 2, 3, 4], [1, 2.1, 1.8, 4.3], 
    linestyle='--', linewidth=2.0, marker='*', markersize=10.0)
#plt.plot([1, 2, 3, 4], [1, 2.1, 1.8, 4.3], '*--')


#- Multiple figure example:

plt.figure(3)
plt.plot([5, 6, 7, 8], [1, 1.8, -0.4, 4.3], marker='o')
plt.figure(4)
plt.plot([0.1, 0.2, 0.3, 0.4], [8, -2, 5.3, 4.2], linestyle='-.')
plt.figure(3)
plt.title('First Plot')


#- Overlay example:

plt.figure(5)
plt.plot([0, 1, 2, 3], [1, 2, 3, 4], '--o',
         [0, 1, 2, 3], [8, -2, 5.3, 4.2], '-.')


#- Call show after all plots are defined:

plt.show()


#===== end file =====
