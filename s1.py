from  PyQt5 import *
from tvtk.tools import mlab
from scipy import *

def f(x,y):
    return sin(x+y)+sin(2*x-y)+cos(3*x+4*y)
    
x = linspace(-5.0,5.0,200)
y = linspace(-5.0,5.0,200)
fig = mlab.figure()
surf = mlab.surfRegularC(x,y,f)
fig.add(surf)