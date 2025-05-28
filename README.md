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

## 🔹 Sub-task 3: Proposed Hybrid Denoising Methods

### Objective:
Propose and implement **novel or hybrid denoising methods from scratch** that better preserve edges while reducing noise.

We propose two advanced strategies:

---

### 1. Edge-Aware Adaptive Filtering with Spatially Varying Smoothing

#### Concept:
Combine edge detection with a spatially adaptive filtering strategy that varies smoothing strength based on **local image variance**:
- Use **Canny Edge Detector** to identify significant edges.
- Compute **local variance** in image patches to assess noise intensity.
- Apply:
  - **Strong smoothing** (e.g., Gaussian) in flat/noisy areas.
  - **Weak or no smoothing** in regions of high variance or near edges.

#### Algorithm Steps:
1. Compute an edge map using the Canny detector.
2. Calculate local variance across the image using sliding windows.
3. Generate a weight map from variance (e.g., normalize to [0,1]).
4. Perform adaptive Gaussian filtering, adjusting kernel size or strength based on the variance and edge map.
5. Merge the smoothed and original image using the adaptive weights and edge mask.

#### Advantages:
- Adapts to image structure and content.
- Strong noise removal in flat regions.
- High fidelity preservation in textured or edge-dense regions.

---

### 2. Iterative Residual Denoising (IRD)

#### Concept:
Apply **multiple passes of denoising** while retaining and refining **residual noise components** to progressively improve image quality.

#### Algorithm Steps:
1. Apply an initial denoising method (e.g., median or wavelet).
2. Compute the residual: `residual = noisy_image - denoised_image`.
3. Apply a secondary denoising to the residual.
4. Add the cleaned residual back to the denoised image.
5. Repeat steps 2–4 for N iterations or until convergence.

#### Advantages:
- Recovers fine textures and details lost in the first pass.
- Gradually reduces structured and unstructured noise.
- Can be combined with other filters (e.g., hybrid of wavelet and NLM).

---

### Evaluation:
- Both methods are evaluated using PSNR and SSIM.
- **Edge-aware filtering** shows superior edge preservation and spatial adaptation.
- **Iterative residual denoising** improves detail recovery and reduces over-smoothing.

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

