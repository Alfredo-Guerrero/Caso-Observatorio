// Función para obtener y mostrar el número de autos
async function fetchAutosCount() {
    try {
        const response = await fetch('/recursoApp/api/count_autos/'); // Ruta completa de la API que cuenta autos
        const data = await response.json();
        const autosCount = data.count;
        document.getElementById('autos_count').innerText = autosCount; // Actualizar el valor del contador de autos
    } catch (error) {
        console.error('Error al obtener el número de autos:', error);
    }
}

// Llamar a la función al cargar la página
fetchAutosCount();
