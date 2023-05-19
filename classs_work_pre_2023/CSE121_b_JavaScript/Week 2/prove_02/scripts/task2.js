/* Lesson 2 */

/* VARIABLES */

// Step 1: declare and instantiate a variable to hold your name
let my_name = 'Steven'

// Step 2: place the value of the name variable into the HTML file (hint: document.querySelector())
document.querySelector('#name').innerHTML = my_name;

// Step 3: declare and instantiate a variable to hold the current year
let current_year = 2022

// Step 4: place the value of the current year variable into the HTML file
document.querySelector('#year').innerHTML = current_year;

// Step 5: declare and instantiate a variable to hold the name of your picture
const my_picture = 'images/me_and_mum.png';

// Step 6: copy your image into the "images" folder

// Step 7: place the value of the picture variable into the HTML file (hint: document.querySelector().setAttribute())
document.querySelector('img').src = my_picture;



/* ARRAYS */

// Step 1: declare and instantiate an array variable to hold your favorite foods
let fav_foods = ['Chomparado','Peanut Butter','Chocolate'];

// Step 2: place the values of the favorite foods variable into the HTML file
document.querySelector('#food').innerHTML = fav_foods;

// Step 3: declare and instantiate a variable to hold another favorite food
let another_food = 'apples';

// Step 4: add the variable holding another favorite food to the favorite food array
fav_foods.push(another_food);

// Step 5: repeat Step 2
document.querySelector('#food').innerHTML = fav_foods;

// Step 6: remove the first element in the favorite foods array
fav_foods.shift();

// Step 7: repeat Step 2
document.querySelector('#food').innerHTML = fav_foods;

// Step 8: remove the last element in the favorite foods array
fav_foods.pop();

// Step 7: repeat Step 2
document.querySelector('#food').innerHTML = fav_foods;


