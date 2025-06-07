# This will contain the implimentation of Edge-and-Variance Adaptive Filter (EVAF)

## Introduction

The goal of this project is to implement a **hybrid denoising algorithm** called the **Edge-and-Variance Adaptive Filter (EVAF)**. The filter intelligently decides which denoising method to apply (median or mean filtering) at each pixel based on:

- The presence of an edge.
- The local variance around a pixel.

This adaptive approach allows for better noise reduction while preserving important image features such as edges and textures.

## Phase 2: Algorithm Design

### Key Components of the EVAF Algorithm

1. **Edge Detection**:
   - Use the Sobel operator to compute the gradient magnitude.
   - Threshold the edge magnitude to detect edge regions.

2. **Local Variance Computation**:
   - Compute local variance using a sliding window (e.g., 3x3).
   - Identify regions with high texture or noise.

3. **Adaptive Filtering Decision**:
   - If a pixel lies in an edge or high-variance region: apply **Median Filter**.
   - Else: apply **Mean Filter**.

This logic ensures that:

- Edges are preserved (median filter prevents blurring),
- Smooth regions are denoised effectively (mean filter removes graininess).

## Phase 3: Implementation and Prototyping

- The implementation is done in Python using OpenCV and NumPy.
- The main script is `evaf_filter.py`.
- The core logic includes:
  - `compute_local_variance()` for local variance estimation.
  - `evaf_filter()` for hybrid filtering.
  - `run_evaf_on_images()` to automate testing across multiple noisy images.

The Home folder contains:

- `barbara.jpg` – Original reference image.

The `Images/` folder contains:

- `barbara_gaussian.png`, `barbara_saltpepper.png`, `barbara_speckle.png` – Noisy variants of the original.
- `Images/evaf_output/` – Stores the denoised outputs.

## Phase 4: Testing & Performance Evaluation

Each denoised image is compared to the original clean image using:

- **PSNR (Peak Signal-to-Noise Ratio)**: Measures reconstruction quality.
- **SSIM (Structural Similarity Index)**: Measures perceptual similarity.

### Example Output

```text
Ground truth loaded: shape=(510, 510)
Loaded noisy image barbara_speckle.png: shape=(510, 510)
Denoised image shape: (510, 510), dtype: uint8
barbara_speckle.png: PSNR=14.26, SSIM=0.2241
Loaded noisy image barbara_saltpepper.png: shape=(510, 510)
Denoised image shape: (510, 510), dtype: uint8
barbara_saltpepper.png: PSNR=24.28, SSIM=0.7800
Loaded noisy image barbara_gaussian.png: shape=(510, 510)
Denoised image shape: (510, 510), dtype: uint8
barbara_gaussian.png: PSNR=22.56, SSIM=0.5518
```

## Phase 4: Testing & Performance Evaluationd

Note : The implementation of this hybrid filtering technique should be done on the various noised Barbara (gaussian, salt-and-pepper and speckle noises) images that are found in the Images/ folder of this repository. This is to ensure that, the computation of testing and performance evaluation is standard so that it can easily be compared with the other filtering techniques (classic and advanced) used before.
