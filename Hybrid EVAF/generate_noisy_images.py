import cv2
import numpy as np
import os

def add_gaussian_noise(image, mean=0, var=0.01):
    row, col = image.shape
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (row, col)) * 255
    noisy = image + gaussian
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_salt_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy = np.copy(image)
    num_salt = np.ceil(salt_prob * image.size)
    num_pepper = np.ceil(pepper_prob * image.size)

    # Salt
    coords = [np.random.randint(0, i, int(num_salt)) for i in image.shape]
    noisy[coords[0], coords[1]] = 255

    # Pepper
    coords = [np.random.randint(0, i, int(num_pepper)) for i in image.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy

def add_speckle_noise(image):
    row, col = image.shape
    noise = np.random.randn(row, col)
    noisy = image + image * noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def save_noisy_images(input_path='Barbara.jpg', output_dir='Images'):
    os.makedirs(output_dir, exist_ok=True)
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    gaussian = add_gaussian_noise(image)
    saltpepper = add_salt_pepper_noise(image)
    speckle = add_speckle_noise(image)

    cv2.imwrite(os.path.join(output_dir, 'barbara_gaussian.png'), gaussian)
    cv2.imwrite(os.path.join(output_dir, 'barbara_saltpepper.png'), saltpepper)
    cv2.imwrite(os.path.join(output_dir, 'barbara_speckle.png'), speckle)

    print("Noisy images saved.")

if __name__ == "__main__":
    save_noisy_images()
