(() => {
    'use strict'
    function readImage(file) {
        if (!file.type || !file.type.match('image\/(png|jpeg|jpg|webp)')) {
            alert("Invalid image format!");
            return;
        }
        if(file.size > 2097152) {
            alert("File is too big!");
            return;
        }

        const img = document.querySelector('#img-card');        
        const reader = new FileReader();
        reader.addEventListener('load', (event) => {
            const imgObj = new Image();
            imgObj.src = event.target.result;
            imgObj.onload = function(ev) {
                if(ev.target.naturalWidth > 512 || ev.target.naturalHeight > 512) {
                    alert("Image max dimesions allowed is 512x512");
                    return;
                }
                img.src = event.target.result;
            }
        });
        reader.readAsDataURL(file);
    }
    document.querySelector('#img-selector')
    .addEventListener('change', function(ev){readImage(ev.target.files[0])})
})()