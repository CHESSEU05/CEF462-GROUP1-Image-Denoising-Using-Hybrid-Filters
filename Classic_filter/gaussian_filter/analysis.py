import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity, mean_squared_error
import matplotlib.pyplot as plt
# Load images
original = cv2.imread('Barbara.jpg', cv2.IMREAD_GRAYSCALE)
noisy = cv2.imread('gaussian_noised_barbara.jpg', cv2.IMREAD_GRAYSCALE)
denoised = cv2.imread('gaussian_denoised_barbara.jpg', cv2.IMREAD_GRAYSCALE)
psnr_noisy = peak_signal_noise_ratio(original, noisy)
psnr_denoised = peak_signal_noise_ratio(original, denoised)

mse_noisy = mean_squared_error(original, noisy)
mse_denoised = mean_squared_error(original, denoised)

print(f"PSNR (Noisy): {psnr_noisy:.2f} dB")
print(f"PSNR (Denoised): {psnr_denoised:.2f} dB")
print(f"MSE (Noisy): {mse_noisy:.4f}")
print(f"MSE (Denoised): {mse_denoised:.4f}")
ssim_noisy = structural_similarity(original, noisy)
ssim_denoised = structural_similarity(original, denoised)

print(f"SSIM (Noisy): {ssim_noisy:.4f}")
print(f"SSIM (Denoised): {ssim_denoised:.4f}")
# Compute gradient magnitude using Sobel
grad_original = cv2.Sobel(original, cv2.CV_64F, 1, 1, ksize=3)
grad_denoised = cv2.Sobel(denoised, cv2.CV_64F, 1, 1, ksize=3)

# Correlation coefficient
edge_preservation = np.corrcoef(grad_original.ravel(), grad_denoised.ravel())[0, 1]
print(f"Edge Preservation Correlation: {edge_preservation:.4f}")
noise_variance = np.var(noisy.astype(float) - original.astype(float))
residual_variance = np.var(denoised.astype(float) - original.astype(float))
reduction_ratio = noise_variance / residual_variance

print(f"Noise Reduction Ratio: {reduction_ratio:.2f}")
