
var url = function(m, pk = null) {
    var r = "/api/v1/" + m + "/";
    if(pk) {
        r += "" + pk + "/";
    }
    return r;
}

var setupRowOverlay = function() {
    $('.overlay-row').mouseover(function() {
        var $divOverlay = $('#div-overlay');
        var $editButton = $('#btn-edit');
        var $deleteButton = $('#btn-delete');

        $editButton.attr("href", $(this).data('url'));

        $deleteButton.popover({
            placement: 'right',
            html: true,
            content: $('#div-delete-popover').html()
        });
        $('#btn-delete-popover').click(function() {
            $.ajax({
                url = $(this).data('url'),
                type: 'DELETE',
            });
        });

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
        $('#btn-delete').popover('hide');
    });
}

$(function() {
    setupRowOverlay();
});
