$('DIV#toggle_header').click(() => {
    if ($(this).hasClass('green')) {
        $(this).addClass('red');
        $(this).removeClass('green');
    } else {
        $(this).removeClass('red');
        $(this).addClass('green');
    }
})