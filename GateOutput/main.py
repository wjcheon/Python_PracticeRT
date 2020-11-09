import numpy as np
import matplotlib.pyplot as plt

rawData = open('3d-pat-proton-Dose_100MEV.raw', 'rb')
rawData_contents = np.fromfile(rawData, dtype=np.float32)

data3D = np.reshape(rawData_contents, ((111,126,126)))
#data2D = data3D[:,20,:]
data2D = data3D[20,:,:]

plt.figure()
plt.imshow(data2D)
plt.show()
