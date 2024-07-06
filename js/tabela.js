var clique = document.querySelector(".clique480");
var celulas = document.querySelector(".dados480");

var clique2 = document.querySelector(".clique640");
var celulas2 = document.querySelector(".dados640");

var clique3 = document.querySelector(".clique800");
var celulas3 = document.querySelector(".dados800");

var clique4 = document.querySelector(".clique960");
var celulas4 = document.querySelector(".dados960");

var clique5 = document.querySelector(".clique1200");
var celulas5 = document.querySelector(".dados1200");

var clique6 = document.querySelector(".clique1600");
var celulas6 = document.querySelector(".dados1600");

var clique7 = document.querySelector(".clique2400");
var celulas7 = document.querySelector(".dados2400");


clique.onclick = function(e) {
    e.preventDefault();
    celulas.classList.toggle('aparecer480');
};

clique2.onclick = function(e) {
    e.preventDefault();
    celulas2.classList.toggle('aparecer640');
};

clique3.onclick = function(e) {
    e.preventDefault();
    celulas3.classList.toggle('aparecer800');
};

clique4.onclick = function(e) {
    e.preventDefault();
    celulas4.classList.toggle('aparecer960');
};

clique5.onclick = function(e) {
    e.preventDefault();
    celulas5.classList.toggle('aparecer1200');
};

clique6.onclick = function(e) {
    e.preventDefault();
    celulas6.classList.toggle('aparecer1600');
};

clique7.onclick = function(e) {
    e.preventDefault();
    celulas7.classList.toggle('aparecer2400');
};