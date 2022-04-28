import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import fits
from spectral_cube import SpectralCube

"""
Data analysis exercise set 3 - Radio spectral data
Author: Tom Carron
"""

hdul = "radio-mapfits.sec"
data=fits.getdata(hdul, ext=0)
header=fits.getheader(hdul)
print(header)
print(data.shape)

image=[]
integrated=np.zeros((5,5))
cum_spec=np.zeros(201)
for i in range(5):
    for j in range(5):
        for k in range(201):
            integrated[i,j]+=data[i,j,k]
            image.append(data[i,j,k])
            cum_spec[k]+=data[i,j,k]

#b. Compute two channel maps by integrating over the frequency channels 50-100 and 100-150.
#Compare the two maps. 10 Points
map1=np.zeros((5,5))
map2=np.zeros((5,5))
for i in range(5):
    for j in range(5):
        k=50
        while k < 101:
            map1[i,j]+=data[i,j,k]
            k+=1
        l=100
        while l < 151:
            map2[i,j]+=data[i,j,l]
            l+=1

#c. Compute the average spectrum, by averaging all 25 positions. 10 Points
avg_spec=cum_spec/25.0





frame=data[:,:,0]
##data = "radio-mapfits.sec"
###cube=SpectralCube.read(data)
##velo, dec, ra = cube.world[:]
x=np.linspace(0,201,201)
fig, ax=plt.subplots(1)
im=ax.imshow(integrated,'cubehelix')
plt.savefig("plots/integrated_intensity_map.png",dpi=400,bbox_inches="tight")
plt.colorbar(im)


fig1, ax1=plt.subplots(1)
im1=ax1.imshow(frame,'cubehelix')
plt.colorbar(im1)

fig2, ax2=plt.subplots(1)
im2=ax2.imshow(map1,'cubehelix')
plt.savefig("plots/map_1.png",dpi=400,bbox_inches="tight")
plt.colorbar(im2)

fig3, ax3=plt.subplots(1)
im3=ax3.imshow(map2,'cubehelix')
plt.savefig("plots/map_2.png",dpi=400,bbox_inches="tight")
plt.colorbar(im3)

fig4, ax4=plt.subplots(1)
im4=ax4.plot(x,avg_spec)#,'cubehelix')
plt.xlabel("channel")
plt.ylabel("Intensity")
plt.savefig("plots/avg_spec.png",dpi=400,bbox_inches="tight")
#plt.colorbar(im4)

#d. Plot every spectrum and overlay the average spectrum. Describe how the emission changes
#across the map. In particular how the line center position, the peak height and the line widths
#behave. 20 Points
#spectra=np.zeros((5,5,201))
#for i in range(5):
    #for j in range(5):
        #for k in range(201):
            #spectra[i,j,k]=data[i,j,k]
plt.show()


for i in range(5):
    for j in range(5):
        fig5, ax5=plt.subplots(1)
        ax5.plot(x,data[i,j,:],color='red')#,label="every spectrum")#,'cubehelix')
        ax5.plot(x,avg_spec,color='black')#,label="average spectrum")
        ax5.set_xlabel("channel")
        ax5.set_ylabel("Intensity")
        plt.savefig("plots/every_spec"+str(i)+"i"+str(j)+"j"+".png",dpi=400,bbox_inches="tight")
#plt.colorbar(im4)



