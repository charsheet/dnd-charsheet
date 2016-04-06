/*
>>>>>>> 80d7f48aaff1a75e14b4155961de7b8863fa0163
$(document).ready(function(){
    $("#str").click(function(){
        $(this).hide();
	});
<<<<<<< HEAD
});
=======
});
*/


$(document).on('show','.accordion', function (e) {
     $('.accordion-heading i').toggleClass(' ');
     $(e.target).prev('.accordion-heading').addClass('accordion-opened');
});

$(document).on('hide','.accordion', function (e) {
    $(this).find('.accordion-heading').not($(e.target)).removeClass('accordion-opened');
    $('.accordion-heading i').toggleClass('fa-chevron-right fa-chevron-down');
});