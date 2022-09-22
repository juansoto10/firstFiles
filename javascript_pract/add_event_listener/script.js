const h1 = document.querySelector('h1');
// const form = document.querySelector('#form');
const input1 = document.querySelector('#calculo1');
const input2 = document.querySelector('#calculo2');
const btn = document.querySelector('#btnCalcular');
const pResult = document.querySelector('#resultado');

// const form = document.querySelector('#form');
// form.addEventListener('submit', concatenaInputValues);
  
function concatenaInputValues(event) {
  console.log({event});
  event.preventDefault();
  //preventDefault(): Coloca en true la propiedad 'defaultPrevented' de, en este caso, el evento 'SubmitEvent' para que no ejecute lo que por defecto debería ejecutar este evento que es la recarga de la página para tratar de enviar en la url la información agregada en el formulario.

  const concatenaInputs = input1.value + input2.value;
  pResult.innerText = 'Resultado: ' + concatenaInputs;
}

btn.addEventListener('click', btnOnClick);

function btnOnClick() {
  const concatenaInputs = input1.value + input2.value;
  pResult.innerText = 'Resultado: ' + concatenaInputs;
}

