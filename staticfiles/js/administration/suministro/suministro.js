$(function () {
   $('#dataSumin').DataTable({
       responsive: true,
       autoWidth: false,
       destroy: true,
       deferRender: true,
       ajax: {
           url: window.location.pathname,
           type: 'POST',
           data: {
               'action': 'search_suministros'
           },
           dataSrc: "",
       },
       columns: [
           {"data": "suministro_empresa.nombre"},
           {"data": "suministro_regional.nombre"},
           {"data": "suministro_sub_estacion.nombre"},
           {"data": "suministro_transformador.marca"},
           {"data": "suministro_alimentadora.nombre"},
           {"data": "cod_sumistro"},
           {"data": "cliente"},
           {"data": "direccion"},
           {"data": "latitud"},
           {"data": "longitud"},
           {"data": "longitud"},
           {"data": "longitud"},
        //    {"data": "suministro_empresa.nombre"},
       ],
       columnDefs: [
        { "width": "10%", "targets": 0 },
        {
            targets: [10],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
             var buttons = '<a href="edit-suministro/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
            //  buttons += '<a href="/suministro/edit-suministro/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="nav-icon fas fa-tachometer-alt"></i></a>';
             return buttons;
            }
        },
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
            //  var buttons = '<a href="/suministro/edit-suministro/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
             buttons = '<a href="medidor/' + row.id + '" class="btn btn-primary btn-xs btn-flat"><i class="nav-icon fas fa-tachometer-alt"></i></a>';
             return buttons;
            }
        },
       ],
       initComplete: function (settings, json) {

       },
   });

});