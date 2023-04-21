// With Javascript Native
const divHeader = document.querySelector('DIV#red_header');
divHeader.addEventListener('click', () => {
    divHeader.style.color = "#FF0000";
});
// With Jquery
$('DIV#red_header').click(() => {
    $(this).css('color', '#FF0000');
})