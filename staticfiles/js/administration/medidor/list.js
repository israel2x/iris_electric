$(function () {
   $('#dataMedidor').DataTable({
       responsive: true,
       autoWidth: false,
       destroy: true,
       deferRender: true,
       ajax: {
           url: window.location.pathname,
           type: 'POST',
           data: {
               'action': 'search_medidor'
           },
           dataSrc: "",
       },
       columns: [
           {"data": "clase"},
           {"data": "marca"},
           {"data": "modelo"},
           {"data": "serie"},
           {"data": "estado"},
           {"data": "suministro.cod_sumistro"},
           {"data": "suministro.cod_sumistro"},
           {"data": "suministro.cod_sumistro"},
           {"data": "suministro.cod_sumistro"},

       ],
       columnDefs: [
        { "width": "10%", "targets": 0 },
        {
            targets: [5],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
             var buttons = '<a href="suministro/medidor/edit-medidor/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
             return buttons;
            }
        },
        {
            targets: [6],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
             buttons = '<a href="administration/medidor/' + row.id + '/detail/" class="btn btn-warning btn-xs btn-flat"><i class="nav-icon fas fa-file"></i></a>';
             return buttons;
            }
        },
            {
               targets: [7],
               class: 'text-center',
               orderable: false,
               render: function (data, type, row) {
               buttons = '<a href="#" class="btn btn-info btn-xs btn-flat"><i class="fa fa-lock"></i></a>';
               return buttons;
               }
         },
            {
               targets: [-1],
               class: 'text-center',
               orderable: false,
               render: function (data, type, row) {
               buttons = '<a href="#" class="btn btn-primary btn-xs btn-flat"><i class="nav-icon fas fa-tachometer-alt"></i></a>';
               return buttons;
               }
         },
       ],
       initComplete: function (settings, json) {

       },
   });

});