// Pop Up

let openPopUp = document.getElementById('open');
let popup = document.getElementById('popUp');
let close = document.getElementById('close');

// Abrir pop up
openPopUp.onclick = function() {
	popup.style.visibility = "visible";
}

// Cerrar pop up
close.onclick = function() {
	popup.style.visibility = "hidden";
}

// Cerrar en ventana y redirigir a una nueva pestaña
popup.onclick = function() {
	popup.style.visibility = "hidden";
}