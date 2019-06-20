$(document).ready( function () {
    $('#table').DataTable({
        "lengthMenu": [[5, 25, 50, -1], [5, 25, 50, "All"]],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        "scrollX": true,
    });
} );

