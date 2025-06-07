
# Edge-and-Variance Adaptive Filter (EVAF) Implementation

## Introduction

The goal of this project is to implement a **hybrid denoising algorithm** called the **Edge-and-Variance Adaptive Filter (EVAF)**. The filter intelligently decides which denoising method to apply (median or mean filtering) at each pixel based on:

- The presence of an edge.
- The local variance around a pixel.

This adaptive approach allows for better noise reduction while preserving important image features such as edges and textures.

## Phase 1: Concept Development & Planning

The initial phase of this project focused on understanding the problem of image denoising and identifying the limitations of existing filtering methods. The goal was to devise a hybrid filtering algorithm that adapts to local image characteristics for improved noise removal and edge preservation.

### Key Objectives in Phase 1

- **Research Existing Filters:** Study common denoising techniques such as mean filtering, median filtering, and advanced filters, understanding their strengths and weaknesses.
- **Identify Challenges:** Recognize issues such as blurring of edges by mean filters and noise persistence in textured regions.
- **Define Hybrid Approach:** Conceptualize a method that combines median and mean filtering based on edge detection and local variance to overcome these challenges.
- **Set Project Scope:** Decide on the Barbara image as the test dataset, types of noise to simulate (Gaussian, salt-and-pepper, speckle), and performance metrics (PSNR, SSIM).
- **Plan Implementation:** Outline the algorithm steps and structure of the codebase, including modules for noise generation, adaptive filtering, and evaluation.

This phase laid the groundwork for designing a practical and effective denoising solution tailored for images with complex textures and edges.

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

- `Barbara.jpg` – Original reference image.

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
barbara_speckle.png: MSE=2465.61, PSNR=14.21, SSIM=0.2246, NRR=64.07%
Loaded noisy image barbara_saltpepper.png: shape=(510, 510)
Denoised image shape: (510, 510), dtype: uint8
barbara_saltpepper.png: MSE=242.76, PSNR=24.28, SSIM=0.7790, NRR=36.43%
Loaded noisy image barbara_gaussian.png: shape=(510, 510)
Denoised image shape: (510, 510), dtype: uint8
barbara_gaussian.png: MSE=358.72, PSNR=22.58, SSIM=0.5542, NRR=42.44%

```

## Phase 5: Installation and Usage

### Installation

Make sure you have Python 3.x installed. Then, install dependencies:

```bash
pip install opencv-python numpy scikit-image
```

### Usage

1. Generate noisy images by running:

```bash
python generate_noisy_images.py
```

2. Run the EVAF filter and evaluate performance:

```bash
python evaf_filter.py
```

---

## Phase 6: Parameters Tuning

You can tune these parameters in `evaf_filter.py` inside the `evaf_filter()` function:

- `edge_thresh` (default 0.1): Edge detection sensitivity.
- `var_thresh` (default 500): Threshold for local variance.
- `ksize` (default 3): Kernel size for Sobel operator and local variance.

Adjust them for your specific use case to improve denoising.

---

## Phase 7: Troubleshooting

- **File Not Found:** Ensure `Barbara.jpg` is in the root directory and images exist in `Images/`.
- **Image Loading NoneType:** Check paths and file extensions.
- **Shape Mismatch:** Ground truth and noisy images must have the same resolution.

---

## License

This project is open source and free to use for educational and research purposes.
