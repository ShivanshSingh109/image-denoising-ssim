function uploadImage() {
    let fileInput = document.getElementById("upload").files[0];
    if (!fileInput) {
        alert("Please upload an image!");
        return;
    }

    let formData = new FormData();
    formData.append("image", fileInput);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        let imgURL = URL.createObjectURL(blob);
        document.getElementById("output").src = imgURL;
        document.getElementById("output").style.display = "block";
        document.getElementById("download").href = imgURL;
        document.getElementById("download").style.display = "block";
    })
    .catch(error => console.error("Error:", error));
}

document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('upload').click();
});