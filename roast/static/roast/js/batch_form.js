var startTime = null;
var roastPoints = [];
var rpRenderer = null;
var apiUrl = "/api/batch/" + pk + "/roastpoints/";

var addRoastpoints = function(d) {
    for(var i = 0; i < d.length; i++) {
        addSinglePoint(d[i]);
    }
}

var addSinglePoint = function(p) {
    roastPoints.push(p);
    if(!rpRenderer) {
        rpRenderer = Tempo.prepare('roastpoints');
    }
    rpRenderer.render(roastPoints);

    if(!p.id) {
        $.post(apiUrl, p, null );
    }
}

$( function() {

    $('#inp-temp').val($('#id_ambient_temp').val())

    $.get("/api/roastevents/", function(d) {
        Tempo.prepare("events").render(d);
    });

    $.get(apiUrl, function(d) {
        addRoastpoints(d);
    });

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

    $('#btn-add').click(function() {
        addSinglePoint( {
            'time': $('#timer-display').html(),
            'temp': $('#inp-temp').val(),
            'batch': { 'id': pk }
        });
    });

    window.setInterval(function() {
        if (startTime) {
            var now = new Date();
            var diff = now - startTime + 250;

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
    }, 1000 );


    // $.get( "/api/orders/", function( data ) {
    //     Tempo.prepare("orders").render(data);
    // });
});
