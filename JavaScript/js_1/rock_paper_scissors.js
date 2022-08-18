function randomChoice() {
    random = Math.floor(Math.random() * options.length);
    rValue = options[random];
    return rValue;
}

const options = ['rock', 'paper', 'scissors'];

let ask = Number(prompt('Please choose: 0-rock, 1-paper or 2-scissors?'));
// console.log(ask);

let choice = options[ask];
let choice2 = randomChoice();

const winMessage = 'You won, luck is on your side this time!';
const loseMessage = 'You lost :C: Maybe you will be lucky next time!';

if (choice !== undefined) {
    console.log(`Player 1: ${choice}\nPlayer 2: ${choice2}`);
}

if (choice === 'rock' && choice2 === 'paper') {
    console.log(loseMessage);
} else if (choice === 'rock' && choice2 === 'scissors') {
    console.log(winMessage);
} else if (choice === 'paper' && choice2 === 'scissors') {
    console.log(loseMessage);
} else if (choice === 'paper' && choice2 === 'rock') {
    console.log(winMessage);
} else if (choice === 'scissors' && choice2 === 'paper') {
    console.log(winMessage);
} else if (choice === 'scissors' && choice2 === 'rock') {
    console.log(loseMessage);
} else if (choice === choice2) {
    console.log("It's a tie. Try again!");
} else {
    console.log('Please enter a valid number (0, 1 or 2)');
}