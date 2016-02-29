<<<<<<< HEAD

$(document).ready(function() {

    var url = $(location).attr('href');
    var qrcode = new QRCode("qrcode",{width:120, height:120});
    if (!url) {
        url = "163.com";
        return;
    }
    qrcode.makeCode(url);
})
=======
$(document).ready(function() {

    function myFlag(){
        $('.my_flag').velocity("fadeOut", {
            duration: 350
    })};

    $('#submit').eq(0).on('click', function(){
        myFlag();
    })

});
>>>>>>> 68a4345640dc1ea35fe17dfc06ae27ef0a215e3e
