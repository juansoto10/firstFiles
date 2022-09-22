const h1 = document.querySelector('h1');
const p = document.querySelector('p');
const parrafito = document.getElementsByClassName('parrafito');
const pid = document.getElementById('pid');
const input = document.querySelector('input');

console.log(input.value);

console.log({
  h1,
  p,
  parrafito,
  pid,
  input,
});

h1.innerHTML = 'Pablito <br> Besten';
p.innerText = 'Texto <br> Otro texto';

console.log(h1.getAttribute('pantalla')); // Obtiene el valor del atributo 'pantalla' del elemento h1. Retornaría: platzilg
h1.setAttribute('class', 'verde'); // Agrega el atributo class con valor 'verde' al elemento h1

h1.classList.add('rojo');
h1.classList.remove('verde');
h1.classList.toggle('verde');
h1.classList.contains('verde');


// Modificar el value y placeholder:

// input.value = '456'
// input.placeholder = 'Sisas mk';


// Crear elementos html: document.createElement('');

console.log(document.createElement('img'));

const img = document.createElement('img');
img.setAttribute('src', 'https://static.platzi.com/static/images/conf/logo_black@2x.png');
console.log(img);


// pid.appendChild(img);
pid.innerHTML = ""; // Borra el texto que hay dentro del párrafo.
pid.append(img);
pid.appendChild(img);

// ESCUCHANDO EVENTOS DESDE JAVASCRIPT