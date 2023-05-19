/* Lesson 5 */

/* IF/ELSE IF */

// Step 1: Declare and initialize a new variable to hold the current date

let current_date = new Date();
console.log(current_date);

// Step 2: Declare another variable to hold the day of the week
// Step 3: Using the variable declared in Step 1, assign the value of the variable declared in Step 2 to the day of the week ( hint: getDay() )

let day_of_week = current_date.getDay();
console.log(day_of_week);

// Step 4: Declare a variable to hold a message that will be displayed
let message =""

// Step 5: Using an if statement, if the day of the week is a weekday (i.e. Monday - Friday), set the message variable to the string 'Hang in there!'
// Step 6: Using an else statement, set the message variable to 'Woohoo!  It is the weekend!'

if (day_of_week == 6 || day_of_week == 0) {
    message ="Woohoo! It's the weekend!";
} else {
    message ="Hang in there!";
}

/* SWITCH, CASE, BREAK */

// Step 1: Declare a new variable to hold another message

second_message =""

// Step 2: Use switch, case and break to set the message variable to the day of the week as a string (e.g. Sunday, Monday, etc.) using the day of week variable declared in Step 2 above

switch (day_of_week) {
    case 0:
        second_message ="Sunday";
        break;
    case 1:
        second_message ="Monday"
        break;
    case 2:
        second_message ="Tuesday"
        break;
    case 3:
        second_message ="Wednesday"
        break;
    case 4:
        second_message ="Thursday"
        break;
    case 5:
        second_message ="Friday"
        break;
    case 6:
        second_message ="Saturday"
        break;
        
}

/* OUTPUT */

// Step 1: Assign the value of the first message variable to the HTML element with an ID of message1

document.querySelector("#message1").innerHTML = message;

// Step 2: Assign the value of the second message variable to the HTML element with an ID of message2

document.querySelector("#message2").innerHTML = second_message;
/* FETCH */
// Step 1: Declare a global empty array variable to store a list of temples

const list_of_temples = [];
// Step 2: Declare a function named output that accepts a list of temples as an array argument and does the following for each temple:
// - Creates an HTML <article> element
// - Appends the <h3> element, the two <h4> elements, and the <img> element to the <article> element as children
// - Appends the <article> element to the HTML element with an ID of temples

function output(temples) {
    let div = document.getElementById("temples");
    // let ul = '<ul id="list_of_temples"></ul>';
    // div.innerHTML = ul;
    // let ulElement = document.getElementById("list_of_temples");
    let ul = document.createElement("ul");
    
    temples.forEach(temple => {
        // - Creates an HTML <h3> element and add the temple's templeName property to it
        let name = temple.templeName;
        let name_item = document.createElement("h3");
        name_item.innerHTML = name;
        ul.appendChild(name_item);

        // - Creates an HTML <h4> element and add the temple's location property to it
        let location = temple.location;
        let location_item = document.createElement("h4");
        location_item.innerHTML = location;
        ul.appendChild(location_item);

        // - Creates an HTML <h4> element and add the temple's dedicated property to it
        let property = temple.dedicated;
        let property_item = document.createElement("h4");
        property_item.innerHTML = property;
        ul.appendChild(property_item);

        // - Creates an HTML <img> element and add the temple's imageUrl property to the src attribute and the temple's templeName property to the alt attribute
        let img = temple.imageUrl;
        let img_item = document.createElement("img");
        img_item.src = img;
        img_item.alt = name;
        ul.appendChild(img_item);
    })

    div.appendChild(ul);
    
    console.log(temples);
}
// Step 3: Create another function called getTemples. Make it an async function.
// Step 4: In the function, using the built-in fetch method, call this absolute URL: 'https://byui-cse.github.io/cse121b-course/week05/temples.json'. Create a variable to hold the response from your fetch. You should have the program wait on this line until it finishes.
// Step 5: Convert your fetch response into a Javascript object ( hint: .json() ). Store this in the templeList variable you declared earlier (Step 1). Make sure the the execution of the code waits here as well until it finishes.
// Step 6: Finally, call the output function and pass it the list of temples. Execute your getTemples function to make sure it works correctly.

async function getTempleData() {
    let responseFromUrl = await fetch('https://byui-cse.github.io/cse121b-course/week05/temples.json');
    templeArray = await responseFromUrl.json();
    output(templeArray);
}

getTempleData()

// Step 7: Declare a function named reset that clears all of the <article> elements from the HTML element with an ID of temples

// Step 8: Declare a function named sortBy that does the following:
// - Calls the reset function
// - Sorts the global temple list by the currently selected value of the HTML element with an ID of sortBy
// - Calls the output function passing in the sorted list of temples

// Step 9: Add a change event listener to the HTML element with an ID of sortBy that calls the sortBy function

/* STRETCH */

// Consider adding a "Filter by" feature that allows users to filter the list of temples
// This will require changes to both the HTML and the JavaScript files
