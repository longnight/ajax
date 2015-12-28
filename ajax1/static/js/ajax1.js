$(document).ready(function() {

    console.log('so far so good');

    $('#comment_1').click(function(){
        $('body').css("background", "#bbffaa");
    })

    $('#comment_2').click(function(){
        $('body').css("background", "lightblue");
    })

    console.log($('.comment').text());

    // var $objlist = $('.comment');
    // console.log($objlist[2];
    // for (var i=1; i<$objlist.length; i++){
        // console.log(typeof $objlist[i])
        // console.log($objlist[i].html());

    // }


});





