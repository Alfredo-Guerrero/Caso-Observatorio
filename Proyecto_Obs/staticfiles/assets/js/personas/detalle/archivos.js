document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('archivo').addEventListener('change', function(e) {
        var fileName = document.getElementById("archivo").files[0].name;
        var nextSibling = e.target.nextElementSibling
        nextSibling.innerText = fileName
    });
});