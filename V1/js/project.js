let menuIcon = document.querySelector('.sidebar');
let navbar = document.getElementsByName('ul');
menuIcon.onclick = () => {
menuIcon.classList.toggle('bx-x');
navbar.classList.toggle('active');
};

const typedUse = new Typed(".usePage", {
  strings: [
    
    "La première étape consiste à renseigner la feuille «liste » par le projet, sa nature ainsi que son emplacement ",
    "En ce qui concerne l’emplacement il dépendrait du lieu de la réalisation de la réunion : ",
    " qui peut être dans ce cas soit le siège ou bien le chantier",
  ],
  typedSpeed: 100,
  backspeed: 100,
  backDelay: 2500,
  loop: true,
});




// //////////////////////////ALERT SAVE/////////////////////
// const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
// const appendAlert = (message, type) => {
//   const wrapper = document.createElement('div')
//   wrapper.innerHTML = [
//     `<div class="alert alert-${type} alert-dismissible" role="alert">`,
//     `   <div>${message}</div>`,
//     '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
//     '</div>'
//   ].join('')

//   alertPlaceholder.append(wrapper)
// }

// const alertTrigger = document.getElementById('liveAlertBtn')
// if (alertTrigger) {
//   alertTrigger.addEventListener('click', () => {
//     appendAlert('SUCCESSFUL SAVED!', 'success')
//   })
// }



///////////////////////ADD new Section Project/////////////////
function initializeSection(
  addBtnId,
  sectionClassName,
  storageKey
) {
  let addBtn = document.getElementById(addBtnId);
  let section = document.querySelector(sectionClassName);
  let addedSections = [];

  // Retrieve sections from local storage when page loads
  if (localStorage.getItem(storageKey)) {
    addedSections = JSON.parse(localStorage.getItem(storageKey));
    addedSections.forEach(() => {
      let clone = section.cloneNode(true);
      section.parentNode.appendChild(clone);
    });
  }

  addBtn.onclick = function() {
    let cloneSection = section.cloneNode(true);
    section.parentNode.appendChild(cloneSection);

    addedSections.push(true);
    localStorage.setItem(storageKey, JSON.stringify(addedSections));
  };
}

// Initialize each section using the function
initializeSection('add-ligne-project', '.first-ligne-project', 'addedSectionsProject');
initializeSection('add-ligne-nature', '.first-ligne-nature', 'addedSectionsNature');
initializeSection('add-ligne-emplacement', '.first-ligne-emplacement', 'addedSectionsEmplacement');
// Repeat for other sections
