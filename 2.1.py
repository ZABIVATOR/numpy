import numpy as np
from PIL import Image
img = Image.open('lunar_images/lunar03_raw.jpg')
data = np.array(img)
data_new = np.zeros(data.shape, dtype = np.uint8)
scale = 255/(data.max()-data.min())
min_data = data.min()
data = (data - min_data) * scale
res_img = Image.fromarray(np.uint8(data))
res_img.show()
#res_img.save("lunar_images/lunar03_raw_upgrade.jpeg")
