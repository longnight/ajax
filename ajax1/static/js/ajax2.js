
$(document).ready(function() {

    var url = $(location).attr('href');
    var qrcode = new QRCode("qrcode",{width:120, height:120});
    if (!url) {
        url = "163.com";
        return;
    }
    qrcode.makeCode(url);
})
