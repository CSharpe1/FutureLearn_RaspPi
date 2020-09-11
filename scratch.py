import numpy as np
import PIL
from PIL import Image
import getopt

opts, args = getopt.getopt(sys.argv, "?hH")

img = Image.open('2bpp.tif')
img.show()

img_arr = np.array(img)

# 2D array
print("shape;",  img_arr.shape)
print("dtype;",  img_arr.dtype)
print(img_arr)
"""
array([[  0,   1,   2, ..., 244, 245, 246],
       [  0,   1,   2, ..., 244, 245, 246],
       [  0,   1,   2, ..., 244, 245, 246],
       ...,
       [  0,   1,   2, ..., 244, 245, 246],
       [  0,   1,   2, ..., 244, 245, 246],
       [  0,   1,   2, ..., 244, 245, 246]], dtype=uint8)
"""
