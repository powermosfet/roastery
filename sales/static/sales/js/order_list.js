$( function() {
    $.get( "/api/orders/", function( data ) {
        Tempo.prepare("orders").render(data);
    });
});
