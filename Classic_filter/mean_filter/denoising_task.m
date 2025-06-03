% --- Task: Implement Speckle Noise and Mean Filter on Barbara.jpg ---

% Define the noising coefficient
noising_coefficient = 0.09;

% 1. Load the Barbara.jpg image
try
    barbara_img = imread('Barbara.jpg');
    % Ensure the image is grayscale if it's not already
    if size(barbara_img, 3) == 3
        barbara_img_gray = rgb2gray(barbara_img);
    else
        barbara_img_gray = barbara_img;
    end
    fprintf('Barbara.jpg loaded successfully.\n');
catch
    error('Error: Barbara.jpg not found or cannot be read. Make sure it is in the same directory.');
end

% Convert to double for calculations
barbara_img_double = im2double(barbara_img_gray);

% 2. Apply speckle noise
% imnoise adds speckle noise with variance specified, here we use the coefficient directly
speckle_noised_barbara = imnoise(barbara_img_double, 'speckle', noising_coefficient);
fprintf('Speckle noise applied successfully.\n');

% 3. Apply the mean filter
% You can define the size of your mean filter (e.g., 3x3)
filter_size = [3 3];
mean_denoised_barbara = imfilter(speckle_noised_barbara, fspecial('average', filter_size));
fprintf('Mean filter applied successfully.\n');

% 4. Display the noisy and denoised images
figure;
subplot(1, 3, 1);
imshow(barbara_img_gray);
title('Original Barbara Image');

subplot(1, 3, 2);
imshow(speckle_noised_barbara);
title('Speckle Noised Barbara');

subplot(1, 3, 3);
imshow(mean_denoised_barbara);
title('Mean Denoised Barbara');

% 5. Export the noisy and denoised images
output_folder = 'mean_filter';
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
    fprintf('Created folder: %s\n', output_folder);
end

imwrite(speckle_noised_barbara, fullfile(output_folder, 'speckle_noised_barbara.jpg'));
imwrite(mean_denoised_barbara, fullfile(output_folder, 'mean_denoised_barbara.jpg'));
fprintf('Noisy and denoised images exported to "%s" folder.\n', output_folder);

fprintf('Task completed successfully!\n');