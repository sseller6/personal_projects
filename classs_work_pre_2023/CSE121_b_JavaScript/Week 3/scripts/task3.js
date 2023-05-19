/* Lesson 3 */

/* FUNCTIONS */

// Function Declaration Section
function add(number1, number2) {
    let sum = number1 + number2;
    return sum;
}
function subtract(number1, number2) {
    let difference = number1 - number2;
    return difference;
}
function multiply(number1, number2) {
    let multiply = number1 * number2;
    return multiply;
}
function divide(number1, number2) {
    let divide = number1 / number2;
    return divide;
}
// Step 3: Step 3: Using function declaration, define another function named addNumbers that gets the values of two HTML form controls with IDs of addend1 and addend2. Pass them to the add function
// Step 4: Assign the return value to an HTML form element with an ID of sum

// use parseInt(), parseFloat(), or Number() when you want to turn a string into a number.

function addNumbers() {
    let num1 = parseFloat(document.querySelector('#addend1').value);
    let num2 = parseFloat(document.getElementById('addend2').value);
    let sum = add(num1,num2);
    document.getElementById('sum').value = sum;
}


// Step 5: Add a "click" event listener to the HTML button with an ID of addNumbers that calls the addNumbers function
//Button V
document.getElementById('addNumbers').addEventListener('click',addNumbers)

// Step 6: Using function expressions, repeat Steps 1-5 with new functions named subtract and subtractNumbers and HTML form controls with IDs of minuend, subtrahend, difference and subtractNumbers

function subtractNumbers() {
    let num1 = parseFloat(document.querySelector('#minuend').value);
    let num2 = parseFloat(document.getElementById('subtrahend').value);
    let difference = subtract(num1,num2);
    document.getElementById('difference').value = difference;
}
//Button V
document.getElementById('subtractNumbers').addEventListener('click',subtractNumbers)

// Step 7: Using arrow functions, repeat Steps 1-5 with new functions named multiply and mulitplyNumbers and HTML form controls with IDs of factor1, factor2, product and multiplyNumbers

function multiplyNumbers() {
    let num1 = parseFloat(document.querySelector('#factor1').value);
    let num2 = parseFloat(document.getElementById('factor2').value);
    let product = multiply(num1,num2);
    document.getElementById('product').value = product;
}
//Button V
document.getElementById('multiplyNumbers').addEventListener('click',multiplyNumbers)

// Step 8: Using any of the three function declaration types, repeat Steps 1-5 with new functions named divide and divideNumbers and HTML form controls with IDs of dividend, divisor, quotient and divideNumbers

function divideNumbers() {
    let num1 = parseFloat(document.querySelector('#dividend').value);
    let num2 = parseFloat(document.getElementById('divisor').value);
    let quotient = divide(num1,num2);
    document.getElementById('quotient').value = quotient;
}
//Button V
document.getElementById('divideNumbers').addEventListener('click',divideNumbers)


/* BUILT-IN METHODS */

// Step 1: Declare and instantiate a variable of type Date to hold the current date

let current_date = '';

// Step 2: Declare a variable to hold the current year

let current_year = '';
// Step 3: Using the variable declared in Step 1, call the built-in getFullYear() method/function and assign it to the variable declared in Step 2
// Step 4: Assign the current year variable to an HTML form element with an ID of year

document.getElementById('year').innerHTML = new Date().getFullYear();

/* ARRAY METHODS */

// Step 1: Declare and instantiate an array variable to hold the numbers 1 through 25

let numbers = [];
for (let i=1; i<=25; i++) {
    numbers.push(i);
}
console.log(numbers);
// Step 2: Assign the value of the array variable to the HTML element with an ID of "array"

document.getElementById('array').innerHTML = numbers;
// Step 3: Use the filter array method to find all of the odd numbers of the array variable and assign the reult to the HTML element with an ID of "odds" ( hint: % (modulus operartor) )

let odds = numbers.filter(n => n%2)

document.getElementById('odds').innerHTML = odds;
// Step 4: Use the filter array method to find all of the even numbers of the array variable and assign the result to the HTML element with an ID of "evens"

let evens = numbers.filter((n) => n % 2 == 0)

document.getElementById('evens').innerHTML = evens;
// Step 5: Use the reduce array method to sum the array variable elements and assign the result to the HTML element with an ID of "sumOfArray"

let sum = numbers.reduce((partialSum, a) => partialSum + a, 0);

document.getElementById('sumOfArray').innerHTML = sum;

// Step 6: Use the map array method to multiple each element in the array variable by 2 and assign the result to the HTML element with an ID of "multiplied"

function multiply2(num) {
    return num * 2
}
document.getElementById('multiplied').innerHTML = numbers.map(multiply2);

// Step 7: Use the map and reduce array methods to sum the array elements after multiplying each element by two.  Assign the result to the HTML element with an ID of "sumOfMultiplied"

let multipliedNumbers = numbers.map(multiply2);

let sumOfMultiplied = multipliedNumbers.reduce((partialSum, a) => partialSum + a, 0);

document.getElementById('sumOfMultiplied').innerHTML = sumOfMultiplied;
