window.onload = function() {
    // Obtener todos los botones
    var buttons = document.querySelectorAll('.btn-app');

    // Iterar sobre los botones
    buttons.forEach(function(button) {
        // Agregar un evento clic a cada botón
        button.addEventListener('click', function() {
            // Obtener el formulario correspondiente al botón
            var formId = button.dataset.formId; // Suponiendo que tengas un atributo personalizado "data-form-id" en cada botón con el ID del formulario correspondiente
            var form = document.getElementById(formId);

            // Resaltar el formulario agregando la clase "highlight"
            form.classList.add('highlight');

            // Establecer un temporizador para eliminar la clase de resaltado después de 3 segundos (3000 milisegundos)
            setTimeout(function() {
                form.classList.remove('highlight');
            }, 3000);
        });
    });
};