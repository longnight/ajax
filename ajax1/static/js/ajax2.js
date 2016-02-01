$(document).ready(function() {

    function myFlag(){
        $('.my_flag').velocity("fadeOut", {
            duration: 350
    })};

    $('#submit').eq(0).on('click', function(){
        myFlag();
    })

});
