function getInput_kk() {
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value; 

  alert(kk_v + " "+ kk_r);
  return kk_v, kk_r;
}

function WriteIntxt(kk_v, kk_r) {
  var userinput = String(kk_v + ": " + kk_r);
  var blob = new Blob([userinput], { type: "text/plain;charset=utf-8"});

  saveAs(blob, "files/vocab.txt");
}

function main() {
  getInput_kk();

  WriteIntxt(getInput_kk.kk_v, getInput_kk.kk_r);
}