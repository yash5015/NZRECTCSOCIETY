var slideImg = document.getElementById("slideImg");

var images = new Array(
  "../static/assets/bg1.jpg",
  "../static/assets/baroda_house.jpg",
  "../static/assets/bg1.jpg",
  "../static/assets/baroda_house.jpg"
);
// var images = new Array(
//   "{%static 'assets/bg1.jpg'%}",
//   "{%static 'assets/baroda_house.jpg'%}",
//   "{%static 'assets/bg1.jpg'%}"
// );
var len = images.length;
var i = 0;

function slider() {
  if (i > len - 1) {
    i = 0;
  }
  slideImg.src = images[i];
  console.log(i);
  i++;

  setTimeout("slider()", 5000);
}
var message = "Commin Soon";
function cmMessage() {
  var cmmessage = document.getElementById("textcmmessage").value;
  window.localStorage.setItem("message", cmmessage);
}

document.getElementById("cmtext").innerHTML = localStorage.getItem("message");

function disableMessage() {
  console.log("hi");
  let ele = document.getElementById("loan-message");
  ele.style.display = "none";
}

function toggleMenu() {
  const menuToggle = document.querySelector(".menuToggle");
  const navigation = document.querySelector(".navigation");

  menuToggle.classList.toggle("active");
  navigation.classList.toggle("active");
}
