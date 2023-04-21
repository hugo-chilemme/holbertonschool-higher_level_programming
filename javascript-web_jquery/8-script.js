$.getJSON( "https://swapi-api.hbtn.io/api/films/?format=json", data => {
    $.each( data.results, function( key, val ) {
        $('UL#list_movies').append(`<LI>${val}</LI>`);
    });
});