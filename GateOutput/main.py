import numpy as np
import matplotlib.pyplot as plt

fileName = '3d-pat-proton-Dose_100MEV.raw'
dim_x = 126
dim_y = 126
dim_z = 111
rawData = open(fileName, 'rb')
rawData_contents = np.fromfile(rawData, dtype=np.float32)
data3D = np.reshape(rawData_contents, ((dim_z,dim_x,dim_y)))

# 2D
selectedSliceNumber =20
data2D = data3D[selectedSliceNumber,:,:]

# Visualization
plt.figure()
plt.imshow(data2D)
plt.show()
