# Test de JavaScript

## Variables

### 1️⃣ Responde las siguientes preguntas:

- ¿Qué es una variable y para qué sirve?

    Son espacios en memoria donde podemos guardar distintos tipos de datos para utilizarlos más adelante.

- ¿Cuál es la diferencia entre declarar e inicializar una variable?

    Declarar una variable es cuando creamos un espacio en memoria para un elemento al que más adelante se le dará un valor, mientras que inicializar es asignarle un valor al elemento para empezar a utiizarlo.

- ¿Cuál es la diferencia entre sumar números y concatenar strings?

    Sumar números es efectuar una operación matemática, mientras que concatenar strings es más como una unión de dos elementos tipo string en un solo elemento del mismo tipo.

- ¿Cuál operador me permite sumar o concatenar?

    El operador + 

### 2️⃣ Determina el nombre y tipo de dato para almacenar en variables la siguiente información:

- Nombre -> String
- Apellido -> String
- Nombre de usuario en Platzi -> String
- Edad -> Number
- Correo electrónico -> String
- Mayor de edad -> Boolean
- Dinero ahorrado -> Number
- Deudas -> Number

### 3️⃣ Traduce a código JavaScript las variables del ejemplo anterior

    let name = 'Juan';
    let lastName = 'Soto';
    let username = 'juansoto10';
    let age = 25;
    let email = 'jpsoto121@gmail.com'
    let adult = true;
    let savedMoney = 1000;
    let debt = 450;

### 4️⃣ Calcula e imprime las siguientes variables a partir de las variables del ejemplo anterior:

- Nombre completo (nombre y apellido)
- Dinero real (dinero ahorrado menos deudas)

Respuesta:

    let fullName = name + ' ' + lastName;
    console.log(fullName); // Juan Soto

    let money = savedMoney - debt;
    console.log(money); // 550

## Funciones

### 1️⃣ Responde las siguientes preguntas en la sección de comentarios:

- ¿Qué es una función?

    Es un conjunto de instrucciones que están encapsuladas y se ejecutan cuando esta es invocada, puede o no recibir argumentos para efectuarse.  Nos permiten guardar bloques de código para reutilizarlos y ejecutarlos en el futuro.

- ¿Cuándo me sirve usar una función en mi código?

    Cuando hay instrucciones que se van a repetir varias veces a lo largo del programa. Esto nos permite reutilizar código,  haciéndolo más legible y compacto.

- ¿Cuál es la diferencia entre parámetros y argumentos de una función?

    Los parámetros son las variables que requiere la función para efectuar las operaciones o instrucciones que se indican dentro de la misma. Los argumentos son los valores que se le dan a estos parámetros cuando se invoca la función.

### 2️⃣ Convierte el siguiente código en una función, pero cambiando cuando sea necesario las variables constantes por parámetros y argumentos en una función:


    const name = "Juan";
    const lastName = "Soto";
    const fullName = name + lastname;
    const nickname = "juansoto10";

    console.log("Mi nombre es " + fullName + ", pero también puedes decirme " + nickname + ".");

Respuesta:

    function presentar(name, lastName, nickname) {
        const fullName = name + lastname;

        console.log("Mi nombre es " + fullName + ", pero también puedes decirme " + nickname + ".");
    }

## Condicionales

### 1️⃣ Responde las siguientes preguntas:

- ¿Qué es un condicional?

    Es un bloque de código donde se pregunta si se cumple una condición determinada y en caso de ser cierto o falso se define si se ejecutan las condiciones especificadas o si se sigue con el flujo del programa.

- ¿Qué tipos de condicionales existen en JavaScript y cuáles son sus diferencias?

    Existen varios: if-else if-else, switch y operador ternario (condición ? expr1 : expr2 )

- ¿Puedo combinar funciones y condicionales?

    Sí, los condicionales nos permiten definir que cosas debe ejecutar una función según que condición se esté cumpliendo.

### 2️⃣ Replica el comportamiento del siguiente código que usa la sentencia switch utilizando if, else y else if:

    const tipoDeSuscripcion = "Basic";

    switch (tipoDeSuscripcion) {
    case "Free":
        console.log("Solo puedes tomar los cursos gratis");
        break;
    case "Basic":
        console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
        break;
    case "Expert":
        console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
        break;
    case "ExpertDuo":
        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
        break;
    }

Respuesta:

    const tipoDeSuscripcion = "Basic";

    if (tipoDeSuscripcion = "Free") {
        console.log("Solo puedes tomar los cursos gratis");
    } else if (tipoDeSuscripcion = "Basic") {
        console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
    } else if (tipoDeSuscripcion = "Expert") {
        console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
    } else if (tipoDeSuscripcion = "ExpertDuo") {
        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
    } else {
        console.log("Ese tipo de suscripción no existe")
    }

### 3️⃣ Replica el comportamiento de tu condicional anterior con if, else y else if, pero ahora solo con if (sin else ni else if).

    if (tipoDeSuscripcion = "Free") {
        console.log("Solo puedes tomar los cursos gratis");
    }
    if (tipoDeSuscripcion = "Basic") {
        console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
    }
    if (tipoDeSuscripcion = "Expert") {
        console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
    }
    if (tipoDeSuscripcion = "ExpertDuo") {
        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
    }

💡 Bonus: si ya eres una experta o experto en el lenguaje, te desafío a comentar cómo replicar este comportamiento con arrays u objetos y un solo condicional. 😏

Respuesta:
```js
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
```

## Ciclos

### 1️⃣ Responde las siguientes preguntas en la sección de comentarios:

- ¿Qué es un ciclo?

    Es una estructura que nos permite repetir una serie de instrucciones, ya sea una cantidad determinada de veces o hasta que cierta condición deje de cumplirse.

- ¿Qué tipos de ciclos existen en JavaScript?

    Existen los ciclos: for, for-in, for-of, while y do-while.

- ¿Qué es un ciclo infinito y por qué es un problema?

    Es aquel ciclo que no termina de ejecutarse nunca debido a que la condición para que este se ejecute siempre se cumple. Es un problema porque no nos lleva a ningún lado y puede bloquear las aplicaciones que se estén usando en el momento debido al alto uso de memoria que ejerce.

- ¿Puedo mezclar ciclos y condicionales?

    Sí, estos nos van a ayudar a definir qué cosas se ejecutan según se requiera.

### 2️⃣ Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:

1.

    for (let i = 0; i < 5; i++) {
        console.log("El valor de i es: " + i);
    }

Respuesta:
    
    let i = 0;

    while (i < 5) {
       console.log("El valor de i es: " + i);
       i++; 
    }

2.

    for (let i = 10; i >= 2; i--) {
        console.log("El valor de i es: " + i);
    }

Respuesta:

    let i = 10;

    while (i >= 2) {
       console.log("El valor de i es: " + i);
       i--; 
    }

### 3️⃣ Escribe un código en JavaScript que le pregunte a los usuarios cuánto es 2 + 2. Si responden bien, mostramos un mensaje de felicitaciones, pero si responden mal, volvemos a empezar. 💡 Pista: puedes usar la función prompt de JavaScript.

```js
//Una forma:

let respuesta;

while(respuesta != 4) {
    let pregunta = prompt("¿Cuánto es 2 + 2?");
    respuesta = pregunta;
}

alert("Felicitaciones, ¡acertaste!");

// ****************************************
// Otra forma:

let respuesta = prompt("¿Cuánto es 2 + 2?");

while(respuesta != 4){
    resultado = prompt("¿Cuanto es 2 + 2?");
}

alert("Felicitaciones, ¡acertaste!");

// ****************************************
// Otra forma más:

let flag = true;

let respuesta;

while (flag) {
    respuesta = prompt("¿Cuánto es 2 + 2?")

    if (suma == 4) {
        alert("Felicitaciones, ¡acertaste!");
        flag = false;
    }
}
```

## Listas

### 1️⃣ Responde las siguientes preguntas en la sección de comentarios:

- ¿Qué es un array?

    Es una colección o agrupación de elementos en una misma variable, cada uno de ellos ubicado por la posición que ocupa en el array.

- ¿Qué es un objeto?

    Un objeto es una estructura de dato que puede incluir colecciones de pares llave-valor (key-value).

- ¿Cuándo es mejor usar objetos o arrays?

    Cuando queramos usar varios datos agrupados ordenadamente y ejecutar acciones con ellos. Permite manejar los datos de una forma más ordenada y evitar crear muchas variables para distintos elementos.

- ¿Puedo mezclar arrays con objetos o incluso objetos con arrays?

    Sí, se pueden tener arrays de objetos u objetos que incluyan arrays.

### 2️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.

    function firstElement(arr) {
        const first = arr.shift();

        console.log(first);
    }

    // Ejemplo: 

    MyArray = ['Cristiano', 'Messi', 'Haaland'];
    firstElement(myArray); 
    
    // Cristiano

### 3️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el array completo).

    function returnElements(arr) {
        for (let i = 0; i < arr.length; i++) {
            console.log(arr[i]);
        }
    }

    // Ejemplo:

    myArray = ['Cristiano', 'Messi', 'Haaland'];
    returnElements(myArray);

    // Cristiano
    // Messi
    // Haaland

### 4️⃣ Crea una función que pueda recibir cualquier objeto como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el objeto completo).

```js
// Forma adecuada: Usando Object.keys() y Object.values() que nos retornan arrays con dichos valores del objeto y luego un ciclo for para imprimirlos

function showElements(obj) {
    arrKeys = Object.keys(obj);
    arrValues = Object.values(obj);

    for (let index = 0; index < arrKeys.length; index++) {
        console.log(`${arrKeys[index]}: ${arrValues[index]}`)
    }
}

// Otra forma:

function returnObjectElements(object) {
    for (let i in object) {
        console.log(`${i}: ${object[i]}`);
    }
}

// Ejemplo (retorna como Strings):

footballPlayers = {
    Cristiano: 'Portugal',
    Messi: 'Argentina',
    Haaland: 'Norway',
}

returnObjectElements(footballPlayers);

// Cristiano: Portugal
// Messi: Argentina
// Haaland: Norway

// Otra forma: 

function showProps(obj) {
    let result = ``;
    for (let i in obj) {
    // obj.hasOwnProperty() se usa para filtrar propiedades de la cadena de prototipos del objeto
    if (obj.hasOwnProperty(i)) {
        result += `${i} = ${obj[i]}\n`;
    }
    }
    console.log(result);
}

showProps(footballPlayers);

// Cristiano: Portugal
// Messi: Argentina
// Haaland: Norway
```