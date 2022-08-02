// 1. A function that determines whether a number is prime or not.


// const primeNumber = (selectedNumber = undefined) => {
//     if(selectedNumber === undefined) return console.warn("You did not enter any value");

//     if(typeof selectedNumber !== "number") return console.error(`You entered something other than a number`);

//     if(selectedNumber === 0) return console.error("0 is not a prime number");

//     if(selectedNumber === 1) return console.error("1 is not a prime number");

//     if(Math.sign(selectedNumber) === -1) return console.error("You entered a negative number");

//     let divisible = false;

//     for(let i = 2; i < selectedNumber; i++) {
//         if((selectedNumber % i) === 0) {
//             divisible = true;
//             break;
//         }
//     }

//     return(divisible)
//         ? console.log(`The number ${selectedNumber} IS NOT a prime number`)
//         : console.log(`The number ${selectedNumber} IS a prime number`);
// }

// primeNumber(); // --> You did not enter any value
// primeNumber("320"); // --> You entered something other than a number
// primeNumber(true); //--> You entered something other than a number
// primeNumber(0) // --> 0 is not a prime number
// primeNumber(1) // --> 1 is not a prime number
// primeNumber(-12) // --> You entered a negative number
// primeNumber(13) // --> The number 13 IS a prime number
// primeNumber(200) // --> The number 200 IS NOT a prime number


// 2. A function that converts degrees Celsius to Fahrenheit


// const convertToF = (degrees = undefined, unit = undefined) => 


// 3. Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

// function showName() {
//     let theName = document.getElementById('typedName');
//     let theNameFixed = theName.value.toLowerCase()
//     console.log(theNameFixed + '\n' + theNameFixed.toUpperCase());
//     let theNameFixed2 = theNameFixed.split(' ')
//     let firstCharUpper = theNameFixed2.map(word => {
//         return word[0].toUpperCase() + word.slice(1)
//     })
//     console.log(firstCharUpper.join(' '))
// }


// 4. A function that returns a reversed string.

// function isPalindrome() {
//     let text = document.getElementById('typedName').value.toLowerCase();

//     let inverted = '';

//     for(let letter of text) {
//         inverted = letter + inverted;
//     }

//     console.log(inverted);
// }


// 5. A function that returns whether a typed word is a palindrome or not.

// function isPalindrome() {
//     let text = document.getElementById('typedName').value.toLowerCase();

//     let inverted = '';

//     for(let letter of text) {
//         inverted = letter + inverted;
//     }

//     console.log(text);
//     console.log(inverted);

//     if(text === inverted) {
//         console.log(`La palabra ${text} SÍ es PALÍNDROMO`);
//     } else {
//         console.log(`La palabra ${text} NO es PALÍNDROMO`);
//     }

// }


// 6. Given an array of integers named -arr- of length -n-, reverse correctly its elements.

// const arr = [1, 2, 3, 4, 5];
// let n = arr.length;

// let l = n - 1;
// let r = 0

// while (l >= r) {
//     arr[l+1] = arr[r];
//     arr[r] = arr[l]
//     console.info(l)
//     console.info(r)

//     l = l - 1;
//     r = r + 1;
// }

// console.log(arr);

/* 

1. arr[0]->4

1. l=0, r=4 --> arr[0] = arr[4]: 5 --> arr[4] = 5
2. l=1, r=3 --> arr[1] = arr[3]: 4 --> arr [3] = 4
3. l=2, r=2 --> arr[2] = arr[2]: 3 --> arr[2] = 3  

*/


// 6. Calculating the pseudo average of an array

// const arr = [1, 2, 3, 4, 5];
// let av = (arr[0] + arr[1])/2;
// let n = arr.length;

// for(let i = 2; i <= n-1; i++) {
//     av = av + arr[i]
//     av = av / 2;
// }

// console.log(av); // --> 4.0625


// 7. Given a string named 'word' which is of the length 'n', print all the ocassions where the characters at index 'i' and 'j' (i < j) are the same. For this it uses the function subString which takes a three parameters: The string to take the substring from, the 1st character of the selected substring and the last character of the selected substring. 

let word = 'Zurita';
let n = word.length;

for(let i = 0; i < n - 2; i++) {
    function subString(text, i1, j1) {
        textToPrint = text;
        arrTextToPrint = textToPrint.split(' ');
        for(i1; i1 <= j1; i1++) {
            console.log()
        }
    }
}
