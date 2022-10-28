// recursive function
temp = [];

function getInput_kk() {
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  var userinput = String(kk_v + ": " + kk_r + "\n");

  // test
  alert(userinput);
  return userinput;
}

function push_to_temp(userinput) {
  temp.push(userinput);
  return temp;
}

function create_txt(temp) {
  var blob = new Blob([temp], { type: "text/plain;charset=utf-8" });
  saveAs(blob, "set.txt");
}


