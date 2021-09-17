+ function($) {
    'use strict';

    // UPLOAD CLASS DEFINITION
    // ======================

    var dropZone = document.getElementById('drop-zone');
    var uploadForm = document.getElementById('js-upload-form');
    var upload_btn = document.getElementById("js-upload-submit");

    var startUpload = function(files) {
        console.log('Starting upload ...')
        let formData = new FormData();
        var file = files[0]
        var filename = file.name;
        var filesize = file.size;
        document.cookie = `filesize=${filesize}`;
        formData.append("file", file);
        // Method 1
        // fetch('/upload_file', {method: "POST", body: formData});

        // Method 2
        var request = new XMLHttpRequest();
        upload_btn.classList.add("d-none");

        // request.open("post", "/upload_file");
        request.open("post", "/post_image");
        request.send(formData);
        console.log("Done")
    }

    uploadForm.addEventListener('submit', function(e) {
        var uploadFiles = document.getElementById('js-upload-files').files;
        e.preventDefault()

        startUpload(uploadFiles)
    })

}(jQuery);