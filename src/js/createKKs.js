'use strict';

const EXPORT_FILE_TYPE = 'text/plain;charset=utf-8';

/**
 * Start downloading of your text file
 * @param {string} filename - File's name
 * @param {string} text - Content
 */
const download = (filename, text) => {
  // Create link DOM element
  const element = document.createElement('a');
  // Set content to download as url encoded string
  element.setAttribute('href', `data:${EXPORT_FILE_TYPE},${encodeURIComponent(text)}`);
  // Mark the file to be downloaded, not opened, when you click on it
  element.setAttribute('download', filename);
  // Add style to not be shown, append to the DOM
  element.style.display = 'none';
  document.body.appendChild(element);
  // Force click on it an delete the element
  element.click();
  document.body.removeChild(element);
};

  // saves the values of the entry fields for the KK'S
  var kk_v = document.getElementById("kk_v").value;
  var kk_r = document.getElementById("kk_r").value;

  //produce a String to put the single var together
  var userinput = String(kk_v + ": " + kk_r + "\n");

  //saves the KK to the localstorage
  save_to_webstorage(userinput);
  // adds the userinput (temp KK) to the array
  temp.push(userinput);
}

function create_and_save() {
  // takes the value of an input field and set it as the file name
  var chosen_set = document.getElementById("choose_set").value;

  // Saves the .txt-file
  var blob = new Blob([temp], { type: "text/plain;charset=utf-8" });
  saveAs(blob, chosen_set + ".txt");

  //cleares the temp array to reuse it
  temp = [];
}

// The including of the webstorage
// HERE IT BEGINS!

function save_to_webstorage(userinput) {
  // creates a var to save the title of the set
  var chosen_set = document.getElementById("choose_set").value;
  
  // saves the userinput in the localstorage with the set-title as the value
  localStorage.setItem(userinput, chosen_set);
}

// only for deleting garbage from the webstorage
function clear_storage() {
  localStorage.clear();
}
