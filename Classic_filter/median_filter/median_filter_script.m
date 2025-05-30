% Load original image
original_img = imread('barbara.jpg');

% Convert to grayscale if it’s not already
if size(original_img, 3) == 3
    gray_img = rgb2gray(original_img);
else
    gray_img = original_img;
end

% Add salt-and-pepper noise with noise density 0.09
noisy_img = imnoise(gray_img, 'salt & pepper', 0.09);

% Apply median filter with 3x3 kernel
denoised_img = medfilt2(noisy_img, [3 3]);

% Save images
imwrite(noisy_img, 'noised_barbara.jpg');
imwrite(denoised_img, 'median_denoised_barbara.jpg');

% Display images
figure;
subplot(1,3,1); imshow(gray_img); title('Original Image');
subplot(1,3,2); imshow(noisy_img); title('Noised Image');
subplot(1,3,3); imshow(denoised_img); title('Median Denoised Image');
% ---------------------------
% Evaluate Denoising Quality
% ---------------------------

% Calculate MSE (Mean Squared Error)
mse_value = immse(denoised_img, gray_img);

% Calculate PSNR (Peak Signal-to-Noise Ratio)
psnr_value = psnr(denoised_img, gray_img);

% Calculate SSIM (Structural Similarity Index)
ssim_value = ssim(denoised_img, gray_img);

% Display metrics
fprintf('MSE: %.4f\n', mse_value);
fprintf('PSNR: %.2f dB\n', psnr_value);
fprintf('SSIM: %.4f\n', ssim_value);