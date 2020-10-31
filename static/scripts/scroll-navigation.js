var logo = document.getElementById('header_logo');
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 50 ||
        document.documentElement.scrollTop > 50
    ) {
        logo.classList.add('logo_animation');
        logo.classList.remove('logo_animation_back');
    } else {
        logo.classList.remove('logo_animation');
        logo.classList.add('logo_animation_back');
    }
}
