const icons = document.getElementById('icons');
const items = document.getElementById('items');


// Agrega un event listener al SVG para detectar clics
icons.addEventListener('click', function() {
    icons.style.fill = '#E51954'; // Cambia a fucsia
});

// Agrega un event listener al SVG para detectar clics
items.addEventListener('click', function() {
    items.style.border = "2px #000 solid";
    ; // Cambia a amarillo
});