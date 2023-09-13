// // Check if the date is already stored in local storage
// let formattedDateTime = localStorage.getItem('formattedDateTime');

// // If not, generate and store the current date and time
// if (!formattedDateTime) {
//   const currentDate = new Date();
//   const day = String(currentDate.getDate()).padStart(2, '0');
//   const month = String(currentDate.getMonth() + 1).padStart(2, '0');
//   const year = currentDate.getFullYear();
//   const hours = String(currentDate.getHours()).padStart(2, '0');
//   const minutes = String(currentDate.getMinutes()).padStart(2, '0');
//   const seconds = String(currentDate.getSeconds()).padStart(2, '0');
//   formattedDateTime = `${day}/${month}/${year} - ${hours}:${minutes}:${seconds}`;

//   // Store the formatted date and time in local storage
//   localStorage.setItem('formattedDateTime', formattedDateTime);
// }

// // Get a reference to the th element by its class name
// const currentDateTh = document.getElementsByClassName('selectedDate')[0]; // Assuming there's only one element with this class

// // Update the content of the th element with the stored date and time
// currentDateTh.textContent = formattedDateTime;














///////////////////////ADD new Section Project/////////////////
// function initializeSection(
// addBtnId,
// sectionClassName,
// storageKey
// ) {
// let addBtn = document.getElementById(addBtnId);
// let section = document.querySelector(sectionClassName);
// let addedSections = [];

// // Retrieve sections from local storage when page loads
// if (localStorage.getItem(storageKey)) {
// addedSections = JSON.parse(localStorage.getItem(storageKey));
// addedSections.forEach(() => {
//   let clone = section.cloneNode(true);
//   section.parentNode.appendChild(clone);
// });
// }

// addBtn.onclick = function() {
// let cloneSection = section.cloneNode(true);
// section.parentNode.appendChild(cloneSection);

// addedSections.push(true);
// localStorage.setItem(storageKey, JSON.stringify(addedSections));
// };
// }

// // Initialize each section using the function
// initializeSection('add-ligne-project', '.first-ligne-project', 'addedSectionsProject');
// initializeSection('add-ligne-nature', '.first-ligne-nature', 'addedSectionsNature');
// initializeSection('add-ligne-emplacement', '.first-ligne-emplacement', 'addedSectionsEmplacement');
// // Repeat for other sections

// document.getElementById('success-save').addEventListener('click', function(event) {
//   event.preventDefault();
//   var projetName = document.querySelector('.selected-project').value; // Get the value from your textarea
//   var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get the CSRF token
  
//   var xhr = new XMLHttpRequest();
//   xhr.open('POST', '{% url "creer_projet" %}', true);
//   xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
  
//   xhr.onreadystatechange = function() {
//       if (xhr.readyState === XMLHttpRequest.DONE) {
//           if (xhr.status === 200) {
//               // Assuming you have a way to reload the table content
//               // Here, reload the whole page as an example
//               location.reload();
//           } else {
//               // Handle error, if needed
//           }
//       }
//   };
  
//   var formData = 'csrfmiddlewaretoken=' + encodeURIComponent(csrfToken) + '&projet-text=' + encodeURIComponent(projetName);
//   xhr.send(formData);
// });





// let sidebar = document.querySelector('.menu-item');
// sidebar.onclick = function() {
//   sidebar.classList.toggle('active');
// }
// console.log("hwllo")
// JavaScript code to handle sidebar active state

// JavaScript code to handle sidebar active state

// JavaScript code to handle sidebar active state

// Function to set the active item in local storage
function setActiveItem(item) {
  localStorage.setItem('activeItem', item);
}

// Function to get the active item from local storage
function getActiveItem() {
  return localStorage.getItem('activeItem');
}

// Add a click event listener to all menu items
const menuItems = document.querySelectorAll('.menu-item');

menuItems.forEach(function(item) {
  item.addEventListener('click', function() {
    // Remove 'active' class from all menu items
    menuItems.forEach(function(menuItem) {
      menuItem.classList.remove('active');
    });

    // Add 'active' class to the clicked item
    item.classList.add('active');

    // Save the active item in local storage
    setActiveItem(item.querySelector('.nav-item').textContent);
  });
});

// On page load, set the active item if it exists in local storage
document.addEventListener('DOMContentLoaded', function() {
  const activeItemText = getActiveItem();
  if (activeItemText) {
    menuItems.forEach(function(item) {
      if (item.querySelector('.nav-item').textContent === activeItemText) {
        item.classList.add('active');
      }
    });
  }
});




// // Select all menu items with the "menu-item" class.
// const menuItems = document.querySelectorAll('.menu-item');

// // Add click event listeners to each menu item.
// menuItems.forEach((menuItem) => {
//   menuItem.addEventListener('click', () => {
//     // Remove the "active" class from all menu items.
//     menuItems.forEach((item) => {
//       item.classList.remove('active');
//     });
// console.log(menuItem)
//     // Add the "active" class to the clicked menu item.
//     menuItem.classList.add('active');
//   });
// });


let form_field_projet = document.querySelector('#id_projet')
form_field_projet.placeholder='Nom du projet que vous souhaitez filtrer';



let form_field_objectif = document.querySelector('#id_obj')
form_field_objectif.placeholder='Ecrit l\'objectif que vous souhaitez filtrer';


