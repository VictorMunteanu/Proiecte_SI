import numpy as np
import matplotlib.pyplot as plt

# Ex a
# img = np.array([np.load(r"images/car_{idx}.npy".format(idx=i)) for i in range(9)])
# print(images)

# Ex b
# suma = np.sum(img)
# print(suma)

# Ex c
# e_sum = np.sum(img, axis=(1,2))
# print(e_sum)

# Ex d
# print(np.argmax(np.sum(img, axis=(1,2))))

# Ex e
from skimage import io
# mean_image = np.mean(img, axis=0)
# io.imshow(mean_image.astype(np.uint8))
# io.show()

# Ex f
# deviat = np.std(img)
# print(deviat)

# Ex g
# normalize = (img - mean_image) / np.std(img)
# print(normalize)

# Ex h
# cropped = img[:, 200:301, 290:401]
# plt.imshow(img[7].astype(np.uint), cmap='gray')
# plt.imshow(cropped[7].astype(np.uint), cmap='gray')