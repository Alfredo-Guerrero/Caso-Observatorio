document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('archivod').addEventListener('change', function(e) {
        var fileName = document.getElementById("archivod").files[0].name;
        var nextSibling = e.target.nextElementSibling
        nextSibling.innerText = fileName
    });
});