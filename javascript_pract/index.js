// 1.

// function firstElement(arr) {
//     const first = arr.shift();

//     console.log(arr);
//     console.log(first);
// }

// myArray = ['Cristiano', 'Messi', 'Haaland'];
// firstElement(myArray);

// 2.

// function returnElements(arr) {
//     for (let i = 0; i < arr.length; i++) {
//         console.log(arr[i]);
//     }
// }

// // Ejemplo:

// myArray = ['Cristiano', 'Messi', 'Haaland'];
// returnElements(myArray);

// Cristiano
// Messi
// Haaland

// 3.0.

// function returnObjectElements(object) {
//     for (let i in object) {
//         console.log(`${i}: ${object[i]}`);
//     }
// }

// const footballPlayers = {
//     Cristiano: 'Portugal',
//     Messi: 'Argentina',
//     Haaland: 'Norway',
// }

// returnObjectElements(footballPlayers);

// 3.1.

// function showProps(obj) {
//     let result = ``;
//     for (let i in obj) {
//       // obj.hasOwnProperty() se usa para filtrar propiedades de la cadena de prototipos del objeto
//       if (obj.hasOwnProperty(i)) {
//         result += `${i} = ${obj[i]}\n`;
//       }
//     }
//     console.log(result);
// }

// const footballPlayers = {
//     Cristiano: 'Portugal',
//     Messi: 'Argentina',
//     Haaland: 'Norway',
// }

// function showElements(obj) {
//     arrKeys = Object.keys(obj);
//     arrValues = Object.values(obj);

//     for (let index = 0; index < arrKeys.length; index++) {
//         console.log(`${arrKeys[index]}: ${arrValues[index]}`)
//     }
// }

// showElements(footballPlayers);

// CONDICIONALES

const tipoDeSuscripcion = {
    Free: 'Solo puedes tomar los cursos gratis',
    Basic: 'Puedes tomar casi todos los cursos de Platzi durante un mes',
    Expert: 'Puedes tomar casi todos los cursos de Platzi durante un año',
    ExpertPlus: 'Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año',
} 

function caracteristicasSuscripción(suscripcion) {
    if (tipoDeSuscripcion[suscripcion]) {
        console.log(tipoDeSuscripcion[suscripcion]);
        return;
    }

    console.warn('Ese tipo de suscripción no existe')
}

caracteristicasSuscripción('Free');