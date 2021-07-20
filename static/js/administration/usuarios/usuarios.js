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
       ],
       columnDefs: [
        { "width": "10%", "targets": 0 }
        //    {
        //        targets: [0],
        //        class: 'text-center',
        //        orderable: false,
        //        render: function (data, type, row) {
        //            var ref_code = '<td><a href="/subasta/' + data + '/" class="btn btn-warning btn-xs btn-flat">'+ data + '</a></td> ';
        //            return ref_code;
        //        }
        //    },
       ],
       initComplete: function (settings, json) {

       },
   });

});