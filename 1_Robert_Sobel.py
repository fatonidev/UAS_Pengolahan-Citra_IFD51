import imageio.v3 as imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Membaca gambar grayscale
image = imageio.imread('1_pohon.jpg', mode='L')

# Operator Roberts dan Sobel
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

def edge_detection(image, kx, ky):
    gx, gy = convolve(image, kx), convolve(image, ky)
    return np.hypot(gx, gy)

roberts_result = edge_detection(image, roberts_x, roberts_y)
sobel_result = edge_detection(image, sobel_x, sobel_y)

# Menampilkan hasil
fig, ax = plt.subplots(1, 3, figsize=(12, 6))
titles = ['Original', 'Roberts', 'Sobel']
images = [image, roberts_result, sobel_result]
for i in range(3):
    ax[i].imshow(images[i], cmap='gray')
    ax[i].set_title(titles[i])
    ax[i].axis('off')
plt.show()
