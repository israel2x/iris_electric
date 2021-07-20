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