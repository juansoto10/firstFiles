// 12. A function that determines whether a number is prime or not.


const primeNumber = (selectedNumber = undefined) => {
    if(selectedNumber === undefined) return console.warn("You did not enter any value");
    
    if(typeof selectedNumber !== "number") return console.error(`You entered something other than a number`);

    if(selectedNumber === 0) return console.error("0 is not a prime number");

    if(selectedNumber === 1) return console.error("1 is not a prime number");

    if(Math.sign(selectedNumber) === -1) return console.error("You entered a negative number");

    let divisible = false;

    for(let i = 2; i < selectedNumber; i++) {
        if((selectedNumber % i) === 0) {
            divisible = true;
            break;
        }
    }

    return(divisible)
        ? console.log(`The number ${selectedNumber} is NOT a prime number`)
        : console.log(`The number ${selectedNumber} IS a prime number`);
}

primeNumber(); // --> You did not enter any value
primeNumber("320"); // --> You entered something other than a number
primeNumber(true); //--> You entered something other than a number
primeNumber(0) // --> 0 is not a prime number
primeNumber(1) // --> 1 is not a prime number
primeNumber(-12) // --> You entered a negative number
primeNumber(13) // --> The number 13 IS a prime number
primeNumber(200) // --> The number 200 is NOT a prime number


// 14. A function that converts degrees Celsius to Fahrenheit


// const convertToF = (degrees = undefined, unit = undefined) => 