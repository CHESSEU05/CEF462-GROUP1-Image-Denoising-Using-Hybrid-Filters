import os
import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def compute_local_variance(img, ksize=3):
    mean = cv2.blur(img, (ksize, ksize))
    squared_mean = cv2.blur(img ** 2, (ksize, ksize))
    variance = squared_mean - mean ** 2
    return variance

def evaf_filter(image, edge_thresh=0.1, var_thresh=500, ksize=3):
    image = image.astype(np.float32)
    sobel_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=ksize)
    sobel_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=ksize)
    edge_magnitude = cv2.magnitude(sobel_x, sobel_y)
    edge_mask = edge_magnitude > edge_thresh * edge_magnitude.max()
    variance_map = compute_local_variance(image, ksize)
    high_variance_mask = variance_map > var_thresh
    output = np.copy(image)
    padded = cv2.copyMakeBorder(image, ksize//2, ksize//2, ksize//2, ksize//2, cv2.BORDER_REFLECT)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            roi = padded[i:i+ksize, j:j+ksize]
            if edge_mask[i, j] or high_variance_mask[i, j]:
                output[i, j] = np.median(roi)
            else:
                output[i, j] = np.mean(roi)
    return output.astype(np.uint8)

def mse(img1, img2):
    return np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)

def noise_power(img_noisy, img_gt):
    noise = img_noisy.astype(np.float32) - img_gt.astype(np.float32)
    return np.mean(noise ** 2)

def noise_reduction_ratio(img_noisy, img_denoised, img_gt):
    noise_before = noise_power(img_noisy, img_gt)
    noise_after = noise_power(img_denoised, img_gt)
    if noise_before == 0:
        return 0.0  # avoid division by zero
    return ((noise_before - noise_after) / noise_before) * 100

def run_evaf_on_images(input_dir='Images', output_dir='Images/evaf_output', ground_truth_path='Barbara.jpg'):
    os.makedirs(output_dir, exist_ok=True)
    
    ground_truth = cv2.imread(ground_truth_path, cv2.IMREAD_GRAYSCALE)
    if ground_truth is None:
        raise FileNotFoundError(f"Ground truth image not found at {ground_truth_path}")
    else:
        print(f"Ground truth loaded: shape={ground_truth.shape}")

    results = []
    for fname in os.listdir(input_dir):
        if fname.startswith('barbara_') and fname.endswith('.png') and 'output' not in fname:
            img_path = os.path.join(input_dir, fname)
            noisy_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if noisy_img is None:
                print(f"Warning: Could not read image {img_path}. Skipping.")
                continue
            else:
                print(f"Loaded noisy image {fname}: shape={noisy_img.shape}")

            denoised = evaf_filter(noisy_img)
            print(f"Denoised image shape: {denoised.shape}, dtype: {denoised.dtype}")

            if ground_truth.shape != denoised.shape:
                print(f"Shape mismatch: ground_truth {ground_truth.shape}, denoised {denoised.shape}. Skipping.")
                continue

            out_path = os.path.join(output_dir, f'evaf_{fname}')
            cv2.imwrite(out_path, denoised)

            psnr_val = psnr(ground_truth, denoised)
            ssim_val = ssim(ground_truth, denoised)
            mse_val = mse(ground_truth, denoised)
            nrr_val = noise_reduction_ratio(noisy_img, denoised, ground_truth)

            results.append((fname, mse_val, psnr_val, ssim_val, nrr_val))
            print(f'{fname}: MSE={mse_val:.2f}, PSNR={psnr_val:.2f}, SSIM={ssim_val:.4f}, NRR={nrr_val:.2f}%')

    return results

if __name__ == "__main__":
    run_evaf_on_images()
