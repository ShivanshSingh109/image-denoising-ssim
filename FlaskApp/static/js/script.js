document.getElementById('uploadButton').addEventListener('click', function () {
    document.getElementById('upload').click();
});

document.getElementById('upload').addEventListener('change', function () {
    let fileInput = document.getElementById("upload").files[0];
    if (fileInput) {
        document.getElementById("fileName").innerText = "Selected: " + fileInput.name;
        document.getElementById("progressBar").style.display = "block";
        document.getElementById("progressBar").value = 0;

        // Auto-start upload
        uploadImage();
    }
});

function uploadImage() {
    let fileInput = document.getElementById("upload").files[0];
    if (!fileInput) {
        alert("Please choose an image first!");
        return;
    }

    let formData = new FormData();
    formData.append("image", fileInput);

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/upload", true);
    xhr.responseType = "blob";  

    // Show the progress bar only when upload starts
    document.getElementById("progressBar").style.display = "block";
    document.getElementById("progressBar").value = 0;

    xhr.upload.onprogress = function (event) {
        if (event.lengthComputable) {
            let percent = (event.loaded / event.total) * 100;
            document.getElementById("progressBar").value = percent;
        }
    };

    xhr.onload = function () {
        if (xhr.status === 200) {
            let blob = xhr.response;
            let imgURL = URL.createObjectURL(blob);
            document.getElementById("output").src = imgURL;
            document.getElementById("output").style.display = "block";
            document.getElementById("download").href = imgURL;
            document.getElementById("download").style.display = "block";
        } else {
            console.error("Upload failed.");
        }
        document.getElementById("progressBar").style.display = "none";
        document.getElementById("upload").value = "";
    };

    xhr.upload.onprogress = function (event) {
        if (event.lengthComputable) {
            let percent = (event.loaded / event.total) * 100;
            requestAnimationFrame(() => {
                document.getElementById("progressBar").value = percent;
            });
        }
    };
    
    xhr.onerror = function () {
        console.error("Error during upload.");
        document.getElementById("progressBar").style.display = "none";
    };

    xhr.send(formData);
}
