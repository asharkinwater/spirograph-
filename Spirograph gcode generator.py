#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Spirograph gcode generator by August Honnell 

import math as m

R = 20 # R, r, d change the shape 
r = 83/6
d = 125/6

print("G28") # home printer 
print("G1 Z10") # lift pen at start
plotter = list()
plotter_1 = list()
angle = 5
theta = .15 
steps = 16 * int(6*3.14/theta) #change step size to make the Spirograph more complex
i = 1
for t in range(0,steps): # loop to genorate gcode 
   
    x = (2*R - r) * m.cos(angle) + d * m.cos((R-r)/(r)*angle)+60  # change values to shange Spirograph shape 
    y = (R - r) * m.sin(angle) - d * m.sin(((R-r)/r)*angle)+60 #before printing, make sure gcode fits your cnc/printer 
    x = round(x, 1) # so you don't crash the 3D printer 
    y = round(y, 1)
    angle = theta + angle 
    if i < 2: # drop pen at start 
        print("G1 "+"X"+str(x)+" Y"+str(y),)
        print("G1 Z0")
        i = i + 1
    else:
        print("G1 "+"X" + str(x) + " Y" + str(y)) # other points 
        i = i + 1
print("G1 Z10")
print("G28")
print(";lines of code = " + str(i)) # lets you know how long the gcode is 


# In[19]:


plotter


# In[ ]:




