

$(document).ready(function() {

    tinymce.init({selector: '#id_content'});

    var $csrf = $('input[name=csrfmiddlewaretoken]:first');
    $csrf.attr('type', 'text');
    $csrf.attr('size', 65);
    $csrf.prop('disabled', true);

    $('.comment_block:even')
        .css("background", "lightyellow")
        .css("font-size", "18px");

    $('.avatar').click(function(){
        if($(this).css('max-width')  == '200px'){
            $(this).animate({'max-width': '800px'}, 200);
        } else {
            $(this).animate({'max-width': '200px'}, 200);
        }
    return false;
    })

    // make ajax post.
    var csrftoken = Cookies.get('csrftoken');
    // console.log(csrftoken);

    $('#submit').click(function(){
        $.post(
            $('#comment_form').attr('action'),
            $('#comment_form').serialize(),
            function(){console.log($('#comment_form').serialize());})
        return false;
    })

});
