## DAY 01
import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
import numpy as np

filename = r"C:\Users\WJCHEON\PycharmProjects\DVH\DB\KIM JEONG SUK\CT\CT.1.3.12.2.1107.5.1.4.66803.30000020052100340807500000018.dcm"
ds = pydicom.dcmread(filename)
img = ds.pixel_array
img_crop = img[300:400, 300:400]
np.shape(img)
np.shape(img_crop)

plt.imshow(img, cmap=plt.cm.bone)
plt.imshow(img_crop, cmap=plt.cm.bone)

## DAY02
import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
import numpy as np
# directory
import os
from os import listdir
from os.path import isfile, join
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


mypath = r"C:\Users\WJCHEON\PycharmProjects\DVH\DB\KIM JEONG SUK\CT"
myFileList = listdir(mypath)
fileNumber= 1
filename = os.path.join(mypath, myFileList[fileNumber])
#filename = r"C:\Users\WJCHEON\PycharmProjects\DVH\DB\KIM JEONG SUK\CT\CT.1.3.12.2.1107.5.1.4.66803.30000020052100340807500000018.dcm"
ds = pydicom.dcmread(filename)
img = ds.pixel_array
img_crop = img[300:400, 300:400]
np.shape(img)
np.shape(img_crop)

plt.imshow(img, cmap=plt.cm.bone)
plt.imshow(img_crop, cmap=plt.cm.bone)
