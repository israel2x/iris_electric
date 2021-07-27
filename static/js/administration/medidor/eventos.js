$(".event-button").on('click', function (e){ 
   e.preventDefault();
   var event = $(this).val();
   var parameters = {
      'event': event,
   }

   // $.ajax({
   //    type: "POST",
   //    url: window.location.pathname,
   //    data: JSON.stringify(parameters),
   //    dataType: 'json',
   //    success: function (response) {
   //          $('#EventsTable tbody').html(response.html_lista_eventos)
   //    },
   //    error: function (response) {
   //       console.log('Ha ocurrido un error');
   //    }
   // });

   $.confirm({
      theme: 'bootstrap',
      title: 'Confirmar!',
      icon: 'fa fa-info',
      content: 'Estas seguro, que desea realizar esta accion?',
      typeAnimated: true,
      columClass: 'medium',
      cancelButtonClass: 'btn-primary',
      draggable: true,
      dragWindowBorder: false,
      buttons: {
          Confirmar: function () {
            btnClass: 'btn-blue',
            $.ajax({
              type: "POST",
              url: window.location.pathname,
              data: JSON.stringify(parameters),
              contentType: 'application/json',
              success: function (response) {
                location.reload();
              },
              error: function (response) {
                 console.log('Ha ocurrido un error');
                  // var err = JSON.parse(response.responseText);
                  //   Swal.fire({
                  //       title: 'Error!',
                  //       html: err.error,
                  //       icon: 'error'
                  //   });
              }
            }); 

          
          },
          Cancelar: function () {
          },
      }
   });

});

