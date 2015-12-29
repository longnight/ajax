$(document).ready(function() {

    var $csrf = $('input[name=csrfmiddlewaretoken]:first');
    $csrf.attr('type', 'text');
    $csrf.attr('size', 65);
    $csrf.prop('disabled', true);

    $('.comment_block:even')
        .css("background", "lightyellow")
        .css("font-size", "18px");

    console.log('so far so good');


    $('#comment_1').click(function(){
        $('body').css("background", "#bbffaa");
    })

    $('#comment_2').click(function(){
        $('body').css("background", "lightblue");
    })

    // var $objlist = $('.comment');
    // console.log($objlist[2];
    // for (var i=1; i<$objlist.length; i++){
        // console.log(typeof $objlist[i])
        // console.log($objlist[i].html());

    // }


});





