var startTime = null;

$( function() {
    var btn = $('#btn-start');

    btn.click(function() {
        if ( btn.hasClass('btn-primary') ) {
            startTime = new Date();

            btn.html('Stop');
            btn.removeClass('btn-primary');
            btn.addClass('btn-danger');
        } else {
            startTime = null;

            btn.html('Start');
            btn.removeClass('btn-danger');
            btn.addClass('btn-primary');
        }
    });

    window.setInterval(function() {
        if (startTime) {
            var now = new Date();
            var diff = now - startTime;

            var hours =   Math.floor(diff/1000/60/60);
            var minutes = Math.floor(diff/1000/60)%60
            var seconds = Math.floor(diff/1000)%60;
            var timerText = "" + ("00" + hours).substr(-2,2)
                         + ":" + ("00" + minutes).substr(-2,2)
                         + ":" + ("00" + seconds).substr(-2,2);

            $('#timer-display').html(timerText);
        }else{
            $('#timer-display').html("00:00:00");
        }
    }, 300);


    // $.get( "/api/orders/", function( data ) {
    //     Tempo.prepare("orders").render(data);
    // });
});
