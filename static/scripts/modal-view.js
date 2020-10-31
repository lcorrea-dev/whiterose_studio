var modal = document.getElementById('myModal');

var imgs = document.getElementsByClassName('screenshot');

var modalImg = document.getElementById('img01');
var captionText = document.getElementById('caption');

for (var img of imgs) {
    img.onclick = function () {
        modal.style.display = 'block';
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    };
}

var span = document.getElementsByClassName('modal')[0];

span.onclick = function () {
    modal.style.display = 'none';
};
