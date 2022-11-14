const signInBtn = document.getElementById("signIn");  
const signUpBtn = document.getElementById("signUp");  
const fistForm = document.getElementById("form1");  
const secondForm = document.getElementById("form2");  
const container = document.querySelector(".container");  
signInBtn.addEventListener("click", () => {  
     container.classList.remove("right-panel-active");  
});  
signUpBtn.addEventListener("click", () => {  
     container.classList.add("right-panel-active");  
});  

//fistForm.addEventListener("submit", (e) => e.preventDefault());  
//secondForm.addEventListener("submit", (e) => e.preventDefault());

"use strict";
const z1 = document.getElementsByClassName("z-1")[0];
const z2 = document.getElementsByClassName("z-2")[0];
const z3 = document.getElementsByClassName("z-3")[0];

const ratio = 0.05;
let x;
let y;

document.addEventListener("mousemove", function (e) {
  x = e.pageX;
  y = e.pageY;
});

requestAnimationFrame(function animation() {
  z1.style.transform = "translate(" + x * ratio + "px," + y * ratio + "px)";

  z2.style.transform =
    "translate(" +
    (x * ratio) / 2 +
    "px," +
    (y * ratio) / 2 +
    "px) rotate(217deg)";

  z3.style.transform =
    "translate(" +
    (x * ratio) / 3 +
    "px," +
    (y * ratio) / 3 +
    "px) rotate(71deg)";

  requestAnimationFrame(animation);
});

