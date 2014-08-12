var startTime = null;
var roastPoints = [];
var rpRenderer = null;
var o_batch = null;

var url = function(m, pk = null) {
    var r = "/api/v1/" + m + "/";
    if(pk) {
        r += "" + pk + "/";
    }
    return r;
}

var addSinglePoint = function(p) {
    if(!rpRenderer) {
        rpRenderer = Tempo.prepare("roastpoints");
    }

    roastPoints.push(p);
    rpRenderer.render(roastPoints);
}

$( function() {

    $('#inp-temp').val($('#id_ambient_temp').val())

    $.get(url("batch", pk), function(d) {
        o_batch = d;

        for(var i = 0; i < d.roastpoint_set.length; i++) {
            $.get(d.roastpoint_set[i], function(rp) {
                addSinglePoint(rp);
            });
        }
    });

    $.get(url("event"), function(d) {
        Tempo.prepare("events").render(d);
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
        var p = {
            'time': $('#timer-display').html(),
            'temp': $('#inp-temp').val(),
            'batch': o_batch.resource_uri
        };
        addSinglePoint(p);
        $.ajax({
            url: url('roastpoint'),
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(p)
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
