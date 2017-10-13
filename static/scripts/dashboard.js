/**
 * Created by Yunzhe on 2017/10/13.
 */

'use strict';
let $img_convert = $('#img_convert');
function convertFormat(t, o) {
    console.log("Here " + o);
    $.get("/convertImage", {'type':t, 'order':o}, function (data) {
        console.log(data);
        $img_convert[0].src = data;
    })
}