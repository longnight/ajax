

$(document).ready(function() {

    // tinymce.init({
    //     selector: '#id_content',
    //     plugins: ["image", "code"],
    //     file_browser_callback: function(field_name, url, type, win) {
    //     if(type=='image') $('#my_form input').click();
    //     }
    // });


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


    var csrftoken = Cookies.get('csrftoken');

    // make ajax post.
    // $('#comment_form #mysubmit').click(function(e){
    //     e.preventDefault();
    //     $.ajax({
    //         type:"POST",
    //         beforeSend: function (request) {
    //             request.setRequestHeader("X-CSRFToken", csrftoken);
    //             request.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest');
    //         },
    //         url: "/comments/",
    //         data: $('#id_content'),
    //     })
    // });


    //RAW xhr POST comment
    var form = $('#comment_form');
    $('#comment_form #mysubmit').click(function(e){
    e.preventDefault();
    xhr = new XMLHttpRequest();
    xhr.open('post', '/comments/', true);

    var data = {"content": "any data work"};
    var form_data;

    console.log(string({"content": "any data work"}));
    xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.send();
    return false;
    })


    // xhr GET content:
    var s_content = '<h3>any word, before</h3>';
    $('#s_content').html(s_content);
    $('#get_s_content').click(function(){
        s_content = '<h3>oh, you clicking on me</h3>';
        $('#loading').show();

        xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function(){
            console.log('state going: %d ', xhr.readyState);
            if (xhr.readyState == 4){
                if (xhr.status >= 200 ){
                    rv = xhr.responseText;
                } else {
                    rv = 'noogood response!'
                }
                $('#loading').hide();
                $('#s_content').html(rv);
            }
        }

        xhr.open('get', '/s/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.send(null);

    })


});
