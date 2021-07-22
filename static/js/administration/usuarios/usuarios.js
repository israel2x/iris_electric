$(function () {
   $('#dataUsers').DataTable({
       responsive: true,
       autoWidth: false,
       destroy: true,
       deferRender: true,
       ajax: {
           url: window.location.pathname,
           type: 'POST',
           data: {
               'action': 'search_usuarios'
           },
           dataSrc: "",
       },
       columns: [
           {"data": "f_name"},
           {"data": "l_name"},
           {"data": "email"},
           {"data": "username"},
           {"data": "perfil"},
           {"data": "perfil"},
           {"data": "perfil"},

       ],
       columnDefs: [
        { "width": "10%", "targets": 0 },
           {
               targets: [5],
               class: 'text-center',
               orderable: false,
               render: function (data, type, row) {
                var buttons = '<a href="/usuarios/edit-user/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';

                return buttons;
               }
           },
           {
            targets: [6],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat"><i class="fa fa-lock"></i></a> ';
                return buttons;
            }
        },
       ],
       initComplete: function (settings, json) {

       },
   });

});