const options = ['rock', 'paper', 'scissors'];1


function getCpuChoice() {
    const random = Math.floor(Math.random() * options.length);
    return options[random];
}

function win(userChoice, cpuChoice) {
    console.log('You won, luck is on your side this time!');
    console.log(`Player 1: ${userChoice}\nCPU: ${cpuChoice}`);
}

function lose(userChoice, cpuChoice) {
    console.log('You lost :C: Maybe you will be lucky next time!');
    console.log(`Player 1: ${userChoice}\nCPU: ${cpuChoice}`);
}

function draw(userChoice, cpuChoice) {
    console.log(`It's a tie. Try again!`);
    console.log(`Player 1: ${userChoice}\nCPU: ${cpuChoice}`);
}

function play(userChoice) {
    const cpuChoice = getCpuChoice();
    switch (userChoice + cpuChoice) {
        case 'rockscissors':
        case 'paperrock':
        case 'scissorspaper':
            win(userChoice, cpuChoice);
            break;
        case 'rockpaper':
        case 'paperscissors':
        case 'scissorsrock':
            lose(userChoice, cpuChoice);
            break;
        case 'rockrock':
        case 'paperpaper':
        case 'scissorsscissors':
            draw(userChoice, cpuChoice);
    }
}

let ask = Number(prompt('Please choose: 0-rock, 1-paper or 2-scissors?'));
let userChoice = options[ask];

play(userChoice);