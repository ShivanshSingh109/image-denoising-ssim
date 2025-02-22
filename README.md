<h2>Features</h2>
<ul>
    <li>Uses Non-Local Means Denoising for noise reduction.</li>
    <li>Applies CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement.</li>
    <li>Computes SSIM to measure similarity with the ground truth image.</li>
    <li>Visualizes results using Matplotlib.</li>
</ul>

<h2>Installation</h2>
<p>Ensure you have Python installed, then install the required dependencies:</p>
<pre><code>pip install opencv-python numpy matplotlib scikit-image</code></pre>

<h2>Usage</h2>
<p>Place your noisy image and ground truth image in the working directory and modify the script to load them:</p>
<pre><code>
<h2>Output</h2>
<p>The output obtained from the script</p>
<img src="https://github.com/ShivanshSingh109/image-denoising-ssim/blob/8869c9b93e7c171f1754bc6a7580200357d58363/OutputImages/1.png" alt="1">
<img src="https://github.com/ShivanshSingh109/image-denoising-ssim/blob/40915dbf5e9e1f783a65d0782774fb373609b224/OutputImages/2.png" alt="2">
<img src="https://github.com/ShivanshSingh109/image-denoising-ssim/blob/40915dbf5e9e1f783a65d0782774fb373609b224/OutputImages/3.png" alt="3">

<p>Additionally, it prints the SSIM score to evaluate the quality of the denoising process.</p>

<h2>Try it Out!</h2>
<p>Try it out here: <a href="https://shivanshsingh.pythonanywhere.com/">Denoise Website</a></p>

<h2>License</h2>
<p>This project is open-source and available under the MIT License.</p>
