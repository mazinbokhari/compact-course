var hover = false;

function activate(panel) {
    $(".panel-primary").map(function() {
        $(this).addClass("panel-default");
        $(this).removeClass("panel-primary");
    });
    $(panel).toggleClass("panel-default");
    $(panel).toggleClass("panel-primary");
}

$('.list-group-item').hover(function() {
    if (!hover) {
        $(this).toggleClass('active');
        hover = true;
    }
}, function() {
    if (hover) {
        $(this).toggleClass('active');
        hover = false;
    }
});

