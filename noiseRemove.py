import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def denoise_image(noisy_image, contrast_factor=0.4):
    lab = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l_denoised = cv2.fastNlMeansDenoising(l, None, h=8, templateWindowSize=7, searchWindowSize=21)
    l_median_filtered = cv2.medianBlur(l_denoised, 3)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    l_contrast_restored = clahe.apply(l_median_filtered)
    l_blended = cv2.addWeighted(l_median_filtered, (1 - contrast_factor), l_contrast_restored, contrast_factor, 0)
    denoised_lab = cv2.merge((l_blended, a, b))
    denoised_image = cv2.cvtColor(denoised_lab, cv2.COLOR_LAB2BGR)

    return denoised_image

# Load images
noisy_image = cv2.imread("input")
ground_truth = cv2.imread("output")

denoised_image = denoise_image(noisy_image, contrast_factor=0.3)
gray_denoised = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)
gray_ground_truth = cv2.cvtColor(ground_truth, cv2.COLOR_BGR2GRAY)
similarity = ssim(gray_denoised, gray_ground_truth, data_range=gray_denoised.max() - gray_denoised.min())

plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.title("Noisy Image")
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title("Denoised Image")
plt.imshow(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 3)
plt.title("Ground Truth")
plt.imshow(cv2.cvtColor(ground_truth, cv2.COLOR_BGR2RGB))

plt.show()

print(f"SSIM After Denoising: {similarity:.4f}")