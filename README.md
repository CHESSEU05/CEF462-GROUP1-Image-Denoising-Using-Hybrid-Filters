# Image Denoising Assignment

This repository contains code and results for an image denoising assignment involving the comparison of classic filters, implementation of advanced denoising approaches, and development of a novel hybrid method to preserve edges while reducing noise.

---

## 🔹 Sub-task 1: Comparison of Classic Filters

### Objective:
Evaluate the performance of three basic filters—Mean, Gaussian, and Median—on images with Gaussian and salt-and-pepper noise.

### Filters:
- **Mean Filter**: Averages pixel values in a local neighborhood. Reduces noise but blurs edges.
- **Gaussian Filter**: Weighted averaging filter that preserves edges better than the mean filter.
- **Median Filter**: Replaces each pixel with the median of its neighborhood. Very effective for salt-and-pepper noise.

### Evaluation Metrics:
- **PSNR (Peak Signal-to-Noise Ratio)**: Measures image quality. Higher is better.
- **SSIM (Structural Similarity Index)**: Measures structural similarity. Closer to 1 is better.

### Key Findings:
- Mean filter reduces Gaussian noise but blurs edges.
- Gaussian filter balances smoothing and edge preservation.
- Median filter is highly effective for salt-and-pepper noise.

---

## 🔹 Sub-task 2: Advanced Denoising Approaches

### 1. Non-Local Means (NLM)
- **Concept**: Averages pixels with similar neighborhoods across the entire image.
- **Implementation**: OpenCV `fastNlMeansDenoising()`
- **Pros**: Excellent detail preservation, ideal for texture-heavy images.
- **Cons**: Computationally intensive.

### 2. Wavelet Denoising
- **Concept**: Applies thresholding in the wavelet domain to suppress noise.
- **Implementation**: PyWavelets (`pywt`)
- **Pros**: Preserves edges and structures; faster than NLM.

### Evaluation:
- NLM and Wavelet both outperform classical filters.
- NLM preserves details best; Wavelet is more efficient.

---

## 🔹 Sub-task 3: Proposed Hybrid Denoising Method

### Method: Adaptive Edge-Preserving Filter

#### Concept:
Combine edge detection and adaptive filtering:
- Use **Canny Edge Detector** to identify edges.
- Apply **strong smoothing** (e.g., Gaussian) to non-edge areas.
- Apply **weaker smoothing** or preserve pixels in edge areas.

#### Steps:
1. Detect edges in noisy image.
2. Create edge mask.
3. Apply Gaussian filter to non-edge areas.
4. Apply Median filter to edge areas or retain original pixels.
5. Combine results using the mask.

#### Advantages:
- Adaptive to image content.
- Strong noise reduction in flat regions.
- Edge preservation where detail is critical.

### Evaluation:
- Compared using PSNR and SSIM.
- Performs better than individual filters by balancing smoothing and detail retention.

---

## 🛠 Technologies Used

- Python
- OpenCV
- scikit-image
- NumPy
- PyWavelets
- Matplotlib

---

## 📊 Results Summary

| Filter Type       | PSNR ↑ | SSIM ↑ | Edge Preservation |
|-------------------|--------|--------|-------------------|
| Mean Filter        | Low    | Low    | Poor              |
| Gaussian Filter    | Medium | Medium | Moderate          |
| Median Filter      | High   | High   | Good              |
| NLM                | Very High | Very High | Excellent     |
| Wavelet Denoising  | High   | High   | Very Good         |
| **Hybrid (Proposed)** | **Very High** | **Very High** | **Excellent** |

---

## 📁 Project Structure

```plaintext
image-denoising-assignment/
│
├── classic_filters/
│   ├── mean_filter.py              # Implementation of mean filter
│   ├── gaussian_filter.py          # Implementation of Gaussian filter
│   └── median_filter.py            # Implementation of median filter
│
├── advanced_methods/
│   ├── nlm_denoising.py            # Non-Local Means filter
│   └── wavelet_denoising.py        # Wavelet thresholding for denoising
│
├── hybrid_method/
│   └── adaptive_edge_preserving.py # Custom hybrid filter combining edge detection
│
├── utils/
│   └── metrics.py                  # PSNR and SSIM calculation utilities
│
├── images/
│   ├── input/                      # Noisy test images
│   └── output/                     # Denoised image results
│
└── README.md                       # Project overview and usage instructions

