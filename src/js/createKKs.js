var temp = new Array();
var str_temp = new String();

function getInput_kk(array = Array()) { // the only function which is working right now :(
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  var userinput = String("\n" + kk_v + ": " + kk_r);

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

  var blob = new Blob([String(temp).split(",")], { type: "text/plain;charset=utf-8" });
  saveAs(blob, "set.txt");
}
