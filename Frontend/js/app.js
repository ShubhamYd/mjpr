  

function amazon(){
	console.log("Amazon OP")
	window.location.href='amazon.html'
  
}


function microsoft(){
	console.log("Microsoft OP")
	window.location.href='microsoft.html'
}

function google(){
	console.log("Google OP")
	window.location.href='google.html'
}

function coda(){
	console.log("Coda OP")
	window.location.href='coda.html'
}

function apple(){
	console.log("Apple OP")
	window.location.href='apple.html'
}

function tesla(){
	console.log("Tesla OP")
	window.location.href='tesla.html'
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "flex";  
  dots[slideIndex-1].className += " active";
}


