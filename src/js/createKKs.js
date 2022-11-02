// the array for saving the KK's until they will putted to a .txt-file
var temp = new Array();

function getInput_kk() {
  // saves the value for the set name
  var chosen_set = document.getElementById("choose_set");

  if (chosen_set !== undefined && chosen_set !== null && chosen_set !== "") {

  } else {
    var none_inp = true;

    do {
      chosen_set = prompt("Bitte geben Sie einen Namen für das Lernset ein:");
      if (chosen_set !== undefined && chosen_set !== null && chosen_set !== "") {
        none_inp = false;
      } else {
        continue;
      }
    } while (none_inp);
  }

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
