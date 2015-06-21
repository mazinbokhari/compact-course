var sectionShown = true;
$('#show-button').click(function() {
    if (sectionShown) {
        $('.section').each(function() {
            $(this).css('display', 'none');
        });
        $('.chapter').each(function() {
            $(this).fadeIn(200);
        });
        $('#show-button').html("Hide Chapters");
        sectionShown = false;
    } else {
        $('.chapter').each(function() {
            $(this).css('display', 'none');
        });
        $('.section').each(function() {
            $(this).fadeIn(200);
        });
        $('#show-button').html("Show Chapters");
        sectionShown = true;
    }

    return false;
});