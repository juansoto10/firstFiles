const h1 = document.querySelector('h1');
const input1 = document.querySelector('#calculo1');
const input2 = document.querySelector('#calculo2');
const btn = document.querySelector('#btnCalcular');
const pResult = document.querySelector('#resultado');


// onchange: Identifica cuando hay cambios en el valor de una etiqueta, en el caso de este ejemplo, un input.

function inputOnChange() {
  console.log('Cambió el input 2');
  // Esto nos imprimiría en consola el mensaje cada que se cambie el valor dentro del input especificado.
}

// onclick: Identifica cuando se da click a un elemento, en este caso, un button.

function btnOnClick() {
  console.log('Escuchando el evento');

  console.log(input1.value + input2.value) 
  // La operación anterior concantenaría strings dado que por defecto los inputs se toman como String

  // console.log(+input1.value + +input2.value);
  // Esto también convertiría a números los inputs, también se puede usar parseInt()

  const sumaInputs = Number(input1.value) + Number(input2.value);

  pResult.innerText = 'Resultado: ' + sumaInputs;
}

