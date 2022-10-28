function getInput_kk() {
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  var userinput = String(kk_v + ": " + kk_r + "\n");

  // test
  alert(userinput);
  return userinput;
}

function push_to_temp(userinput, temp) {
  temp.push(userinput);
}

function create_array(temp) {
  // create var for return value of first function
  var userinput_temp = getInput_kk();
  console.log(userinput_temp); //test
  // pushes the userinput to the array
  var temp = push_to_temp(userinput_temp);
  return temp;
}

function create_txt(temp) {
  var blob = new Blob([temp], { type: "text/plain;charset=utf-8" });
  saveAs(blob, "set.txt");

  temp = [];
}

function main(temp) {
  var final_temp = create_array(temp);
  create_txt(final_temp);
}