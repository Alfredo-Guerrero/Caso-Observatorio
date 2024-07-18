document.getElementById('exportar-pdf').addEventListener('click', function() {
    html2canvas(document.querySelector("#miModal .section-to-export"), {
        scale: 2, // Ajusta la escala para mejorar la calidad
        useCORS: true, // Habilita el uso de CORS para cargar imágenes externas
        scrollY: -window.scrollY, // Soluciona problemas de desplazamiento
    }).then(canvas => {
        // Redimensionar la imagen en el canvas
        var ctx = canvas.getContext('2d');
        ctx.font = "8px Arial"; // Establecer el tamaño de fuente

        var pdf = new jsPDF('p', 'mm', 'a4');
        var imgWidth = pdf.internal.pageSize.getWidth() * 0.90; // Ancho de la página A4 reducido en un 5%
        var imgHeight = canvas.height * imgWidth / canvas.width; // Calcula la altura proporcional
        var x = 10; // Margen izquierdo de 10 mm
        var y = 10; // Margen superior de 10 mm


        pdf.addImage(canvas.toDataURL('image/jpeg', 1.0), 'JPEG', x, y + 30, imgWidth, imgHeight);
        pdf.save('Ficha de Asistencia.pdf');
    });
});