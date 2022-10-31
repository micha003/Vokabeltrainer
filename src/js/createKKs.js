var temp = new Array();

function getInput_kk() { // the only function which is working right now :(
  var kk_v = document.getElementById("kk_v").value;
  var kk_r = document.getElementById("kk_r").value;

  var userinput = String("\n" + kk_v + ": " + kk_r);

  save_to_webstorage(userinput);

  // test
  alert(userinput);

  temp.push(userinput);
  // test
  alert(temp);
}

function create_and_save() {
  getInput_kk(temp);

  // test
  console.log(temp);

  var chosen_set = document.getElementById("choose_set").value;

  var blob = new Blob([temp], { type: "text/plain;charset=utf-8" });
  saveAs(blob, chosen_set + ".txt");

  temp = [];
}

// The including of the webstorage
// HERE IT BEGINS!

function save_to_webstorage(userinput) {
  var chosen_set = document.getElementById("choose_set").value;
  
  localStorage.setItem(chosen_set, userinput);
}
