
var url = function(m, pk = null) {
    var r = "/api/v1/" + m + "/";
    if(pk) {
        r += "" + pk + "/";
    }
    return r;
}

var updateOverlay = function() {
    $("#btn-delete").click( function() {
        $("#btn-delete-confirm").fadeIn();
    });

    $("#btn-delete-confirm").hide();

    $("#btn-delete-confirm").click( function() {
        $.ajax({
            url: $(this).data('url'),
            type: 'DELETE',
            success: function() {
                alert("Deleted it.");
            }
        });
    });

    $('.overlay-row').mouseover(function() {
        var $divOverlay = $('#div-overlay');
        var $editButton = $('#btn-edit');
        var $deleteButton = $('#btn-delete');
        var url = $(this).data("url");

        $editButton.attr("href", url);
        $("#btn-delete-confirm").data("url", url);

        var bottomWidth = $(this).css('width');
        var bottomHeight = $(this).css('height');
        var rowPos = $(this).position();
        var bottomTop = rowPos.top;
        var bottomLeft = rowPos.left;
        $divOverlay.css({
            position: 'absolute',
            display: 'block',
            top: bottomTop,
            left: bottomLeft,
            width: bottomWidth,
            height: bottomHeight
        });
    });

    $('#div-overlay').mouseleave(function() {
        var $divOverlay = $('#div-overlay');
        $divOverlay.hide();
        $('#btn-delete-confirm').hide();
    });
};
