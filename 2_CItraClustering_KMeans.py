import os
import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Mengatasi masalah LOKY_MAX_CPU_COUNT
os.environ["LOKY_MAX_CPU_COUNT"] = "2"

# Membaca gambar dalam mode grayscale
image = imageio.imread('2_gambar.jpg', mode='L')  # mode='L' untuk grayscale
image_reshaped = image.reshape(-1, 1)

# Menggunakan K-Means untuk segmentasi dengan batasan CPU core
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
kmeans.fit(image_reshaped)
segmented = kmeans.labels_.reshape(image.shape)

# Visualisasi hasil segmentasi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Segmented Image")
plt.imshow(segmented, cmap='gray')
plt.show()
