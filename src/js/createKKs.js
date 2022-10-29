function getInput_kk(array = Array()) { // the only function which is working right now :(
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  var userinput = String(kk_v + ": " + kk_r + "\n");

  // test
  alert(userinput);

  array.push(userinput);
  // test
  console.log(array);

  return array;
}

function create_and_save(array = Array()) {
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  var userinput = String(kk_v + ": " + kk_r + "\n");

  // test
  alert(userinput);

  array.push(userinput);
  // test
  console.log(array + "finishing");

  var blob = new Blob([array], { type: "text/plain;charset=utf-8" });
  saveAs(blob, "set.txt");

  return array = [];
}
