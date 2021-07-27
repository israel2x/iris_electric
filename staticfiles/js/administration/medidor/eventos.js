$(".event-button").on('click', function (e){ 
   e.preventDefault();
   var event = $(this).val();
   console.log(event);

   var parameters = {
      'event': event,
   }
   // console.log(parameters);

   $.ajax({
      type: "POST",
      url: window.location.pathname,
      data: JSON.stringify(parameters),
      dataType: 'json',
      success: function (response) {
            // $('#docsTable tbody').html(response.html_lista_documentos)
            // $("#advanced-profile").trigger('reset');
            // $('#hidden-spinner').hide();
            // $('#up_load_btn').show();
      },
      error: function (response) {
            // var err = JSON.parse(response.responseText);
            // Swal.fire({
            //    title: 'Error!',
            //    html: err.error,
            //    icon: 'error'
            // });
      }
   });

});