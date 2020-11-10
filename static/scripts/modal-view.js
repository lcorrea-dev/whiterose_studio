var modal = document.getElementById('myModal');

var imgs = document.getElementsByClassName('screenshot');


var modalImg = document.getElementById('img01');
var caption = document.getElementById('caption');

var authorText = document.getElementById('author');

for (var img of imgs) {
    img.onclick = function () {
        modal.style.display = 'block';
        modalImg.src = this.src;
        caption.innerText= this.nextElementSibling.innerText;
        author.innerHTML= 'by ' + this.nextElementSibling.nextElementSibling.innerHTML
    };
}

var span = document.getElementsByClassName('modal')[0];

span.onclick = function () {
    modal.style.display = 'none';
};
