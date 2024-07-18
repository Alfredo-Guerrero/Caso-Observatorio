    // Función para mostrar la confirmación de eliminación
    function confirmDelete(per_id) {
        Swal.fire({
            title: '¿Estás seguro?',
            text: '¿Estás seguro de que deseas eliminar este registro?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                // Si el usuario confirma, enviar la solicitud de eliminación
                fetch(url_delete.replace('0', per_id), {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': '{{ csrf_token }}'
                        }
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Error al eliminar el personal del sistema');
                        }
                        // Si la eliminación es exitosa, mostrar mensaje de éxito
                        Swal.fire({
                            title: 'Eliminación exitosa',
                            icon: 'success',
                            timer: 5000 // Tiempo de duración en milisegundos (2 segundos en este caso)
                        });
                        // Actualizar la página después de la eliminación exitosa
                        window.location.reload();
                    })
                    .catch(error => {
                        // Si ocurre un error durante la eliminación, mostrar mensaje de error
                        Swal.fire({
                            title: 'Error al eliminar',
                            text: error.message,
                            icon: 'error'
                        });
                    });
            }
        });
    }