temp = new Array();
create_txt = false

function get_status_ckk(variable) {
  variable = true;
  return variable;
}

function getInput_kk() {
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  var userinput = String(kk_v + ": " + kk_r + "\n");

  // test
  alert(userinput);

  // Append the userinput to a temp. storage (Array)
  temp.push(userinput);
  // test
  alert(temp);
  
  if (create_txt) {
    var blob = new Blob([temp_array], { type: "text/plain;charset=utf-8"});

     saveAs(blob, "lernset.txt");
    temp = [];
    return temp;
  }
}


