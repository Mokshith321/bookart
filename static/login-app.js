const mainlogin = document.getElementById("main-login");
const mainsignup = document.getElementById("main-signup");
const promttosignup = document.getElementById("promttosignup");
const promttologin = document.getElementById("promttologin");
var signupbtn = document.getElementById("signupbtn");
var loginbtn = document.getElementById("loginbtn");
const container = document.getElementById("container");

signupbtn.addEventListener("click", ()=>{
    container.classList.add("animation-class");
    promttosignup.style.display = "none";
    mainlogin.style.display = "none";
    mainsignup.style.display= "block";
    promttologin.style.display = "block";
})

loginbtn.addEventListener("click", ()=>{
    promttosignup.style.display = "block";
    mainsignup.style.display= "none";
    mainlogin.style.display = "block";
    promttologin.style.display = "none";
})