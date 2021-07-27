$(".event-button").on('click', function (e){ 
   e.preventDefault();
   var event = $(this).val();
   var parameters = {
      'event': event,
   }

   $.ajax({
      type: "POST",
      url: window.location.pathname,
      data: JSON.stringify(parameters),
      dataType: 'json',
      success: function (response) {
            $('#EventsTable tbody').html(response.html_lista_eventos)
      },
      error: function (response) {
         console.log('Ha ocurrido un error');
      }
   });

});