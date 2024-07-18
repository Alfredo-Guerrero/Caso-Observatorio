        // Función para mostrar el spinner de carga y recargar la tabla
        function recargarTabla() {
            // Mostrar el spinner de carga
            $('#loader').removeClass('d-none');

            // Realizar la llamada AJAX para recargar la tabla
            $.ajax({
                url: urlAsignaciones,
                type: 'GET',
                success: function(data) {
                    // Actualizar el contenido de la tabla con los datos recibidos del servidor
                    $('#dtabla-asignaciones').html(data);

                    // Reinicializar el DataTable después de actualizar los datos
                    reinicializarDataTable();
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.error('Error al recargar la tabla:', errorThrown);
                }
            });

            // Ocultar el spinner de carga después de 2 segundos
            setTimeout(function() {
                $('#loader').addClass('d-none');
            }, 2000); // 2000 milisegundos = 2 segundos
        }

        // Función para reinicializar el DataTable
        function reinicializarDataTable() {

            var table2 = $('#dataTable2').DataTable({
                dom: 'Blfrtip',
                buttons: [
                    'excel', 'print'
                ],
                "language": {
                    "lengthMenu": "Mostrar _MENU_ registros por página",
                    "zeroRecords": "No se encontraron registros",
                    "info": "Mostrando _PAGE_ de _PAGES_ páginas",
                    "infoEmpty": "No hay registros disponibles",
                    "infoFiltered": "(filtrado de _MAX_ registros totales)",
                    "search": "Buscar:",
                    "paginate": {
                        "next": "Siguiente",
                        "previous": "Anterior"
                    }
                },
                "paging": true,
                "searching": true,
                "responsive": false,
                "ordering": true,
                "pageLength": 20,
                "lengthMenu": [
                    [20, 50, 100, -1],
                    [20, 50, 100, "Todos"]
                ]
            });

            table2.buttons().container()
                .find('.dt-button').removeClass('dt-button').addClass('btn btn-sm')
                .each(function() {
                    var btnClass = '';
                    var btnIcon = '';
                    var btnText = $(this).text();
                    switch (btnText) {

                        case 'Excel':
                            btnClass = 'btn-dark';
                            btnIcon = 'fas fa-file-excel';
                            break;
                        case 'Print':
                            btnClass = 'btn-dark mr-2';
                            btnIcon = 'fas fa-print';
                            break;
                    }
                    $(this).addClass(btnClass);
                    $(this).html('<i class="' + btnIcon + '"></i> ' + btnText);
                });


            // Reajustar el encabezado fijo
            new $.fn.dataTable.FixedHeader(table);
        }

        // Llamar a la función para reinicializar el DataTable cuando se carga la página
        $(document).ready(function() {
            reinicializarDataTable();
        });

        // Cuando se hace clic en el botón de recargar, llamar a la función recargarTabla
        $('#btn-recargar').on('click', function() {
            recargarTabla();
        });