$(document).ready(function(){
    $('.one-post').hover(function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.1'}, 300);
    }, function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
    });

    var logoImg = $('.header img');
    var originalWidth = logoImg.width();
    var originalHeight = logoImg.height();

    logoImg.hover(function(){
        $(this).animate({width: originalWidth + 20, height: originalHeight + 20}, 300);
    }, function(){
        $(this).animate({width: originalWidth, height: originalHeight}, 300);
    });
});
