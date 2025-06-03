import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
# Load the grayscale image
image_path = "Barbara.jpg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Barbara.jpg not found.")
# Add Gaussian noise
noise_std = 0.09 * 255  # because image pixel values range from 0–255
noise = np.random.normal(0, noise_std, img.shape)
noisy_img = img + noise

# Clip values to valid range [0, 255] and convert to uint8
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

# Save the noisy image
cv2.imwrite("gaussian_noised_barbara.jpg", noisy_img)
# Apply Gaussian filter to denoise
denoised_img = gaussian_filter(noisy_img, sigma=1)

# Convert and save
denoised_img = np.clip(denoised_img, 0, 255).astype(np.uint8)
cv2.imwrite("gaussian_denoised_barbara.jpg", denoised_img)
print(" Noised and denoised images saved successfully.")
