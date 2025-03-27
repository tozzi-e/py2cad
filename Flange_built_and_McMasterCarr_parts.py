from build123d import *
from ocp_vscode import show
import numpy as np 

 
# Ferrule https://www.mcmaster.com/4759K266/ Extra-High-Polish Metal Quick-Clamp Tube Fitting Sanitary, for 1.5" OD Tube x Butt-Weld Tube, 1-1/8" Long
# Bolts   92185A634  Super-Corrosion-Resistant 316 Stainless Steel Socket Head Screw, 3/8"-16 Thread Size, 2-1/2" Long, Partially Threaded
# Nuts    90372A332  18-8 Stainless Steel Socket Nut 3/8"-16 Thread Size
# O-ring  9263K736   # note slightly less ID than the E&H part - Chemical-Resistant Viton® Fluoroelastomer O-Ring, 3 mm Wide, 42 mm ID
#fitment tested with 3d printed part

ferr_ID=25.4*1.37

#base roounded rectangle
sk1=Pos(0,0,0)*RectangleRounded(74,74,12)
ex1 =extrude(sk1,amount=20)

#remove ID of ferrule
ex1=ex1-Pos(0,0,10)*Cylinder(34.798/2,20)

#Remove cylinders to create bolt holes
for i in [-49/2,49/2]:
    for j in [-49/2,49/2]:

        ex1=ex1-Pos(i,j,10)*Cylinder(10.3/2,20)

# Remove first cylindrical volume to creat cavity that connects with the DPT 
ex1=ex1-Pos(0,0,1.4/2)*Cylinder(55.05/2,1.4)

# Remove second cylinderical volume to create cavity that houses the o-ring 
ex1=ex1-Pos(0,0,(1.4+4)/2)*Cylinder(49.6/2,1.4+4)

#create fillet to make o-ring more washable
edgecir0=ex1.edges().filter_by(GeomType.CIRCLE).group_by(SortBy.RADIUS)[2]
edgecir=edgecir0.sort_by(Axis.Z)[0]
ex1= fillet(edgecir,2.5)

#Remove cylindrical volume where the ferrule OD goes in
ex1=ex1-Pos(0,0,15)*Cylinder(25.4*1.5/2,10)

 
#Remove cylinders to create the cavity for Bolt heads/Nuts
for i in [-49/2,49/2]:
    for j in [-49/2,49/2]:
        ex1=ex1-Pos(i,j,15)*Cylinder(15.4/2,10)


show(ex1 )
ex1.export_step("flanges5_xom3.step")