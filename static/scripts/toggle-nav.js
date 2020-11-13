var burger = document.querySelector('.burger');
var navList = document.querySelector('.horizontallist');

function toggleNav() {
    navList.classList.toggle('nav-open');
}

burger.addEventListener('click', function () {
    toggleNav();
});
