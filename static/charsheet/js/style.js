/*
$(document).ready(function() {
    $('button').click(function() {
        $('.vanish').fadeOut('slow');
    });
});

$(document).ready(function() {
    $('div').click(function() {
        $(this).fadeOut('slow');
    });
});

$(document).ready(function() {
    $('.pull-me').click(function() {
        $('.panel').slideToggle('slow')
    });
});

*/

$(function (){
    if($('#character').val()== "true"){
         $("input:checkbox").prop('checked',true);
    }else{
        $("input:checkbox").prop('checked', false);
    }
});
