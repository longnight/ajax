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

    var flag = true;
    $('.avatar').click(function(){
        $(this).stop().animate({height: (flag ? "500px" : "250px") }, 'fast');
        flag = !flag;
        // $('.avatar').css('max-width', '500px')
    })


});





