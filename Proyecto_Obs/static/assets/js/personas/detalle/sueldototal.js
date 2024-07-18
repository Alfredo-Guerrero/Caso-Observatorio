  // Función para calcular el total
  function calcularTotal() {
      var cantidad = parseFloat(document.getElementById('cantidad').value);
      var sueldo = parseFloat(document.getElementById('importe').value);
      var total = cantidad * sueldo;

      // Verificar si el total es un número válido
      if (!isNaN(total)) {
          document.getElementById('total').value = total.toFixed(2); // Redondear el total a 2 decimales
      }
  }

  // Escuchar los cambios en los campos de cantidad y sueldo
  document.getElementById('cantidad').addEventListener('input', calcularTotal);
  document.getElementById('importe').addEventListener('input', calcularTotal);