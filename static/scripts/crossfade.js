var top_img = document.getElementById('character_top');
var bot_img = document.getElementById('character_bottom');

top_img.addEventListener('mouseover', function () {
    top_img.style.opacity = 0;
    bot_img.style.opacity = 1;
});

top_img.addEventListener('mouseout', function () {
    top_img.style.opacity = 1;
    bot_img.style.opacity = 0;
});
