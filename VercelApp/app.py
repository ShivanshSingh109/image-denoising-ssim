from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def denoise_image(image_path):
    noisy_image = cv2.imread(image_path)
    
    if noisy_image is None:
        return None
    
    lab = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l_denoised = cv2.fastNlMeansDenoising(l, None, h=8, templateWindowSize=7, searchWindowSize=21)
    l_median_filtered = cv2.medianBlur(l_denoised, 3)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    l_contrast_restored = clahe.apply(l_median_filtered)
    l_blended = cv2.addWeighted(l_median_filtered, 0.7, l_contrast_restored, 0.3, 0)
    denoised_lab = cv2.merge((l_blended, a, b))
    denoised_image = cv2.cvtColor(denoised_lab, cv2.COLOR_LAB2BGR)

    output_path = os.path.join(PROCESSED_FOLDER, "denoised.jpg")
    cv2.imwrite(output_path, denoised_image)
    return output_path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    output_path = denoise_image(filepath)
    
    if output_path:
        return send_file(output_path, mimetype='image/jpeg')
    else:
        return "Error processing image", 500

if __name__ == '__main__':
    app.run(debug=True)
