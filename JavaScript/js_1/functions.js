// Declarativas / Function declaration / Function statement

function myFunction() {
    return 'Hola, Estamos aprendiendo JS';
}

console.log(myFunction());

// --> Hola, Estamos aprendiendo JS


// De expresión / Anónimas/ Function expression

var myFunction = function(x, y) {
    return x + y;
}

console.log(myFunction(10,23));

// --> 33