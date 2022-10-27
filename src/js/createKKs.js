function getInput_kk() {
  var kk_v = document.input_kk.input_kk_v.value;
  var kk_r = document.input_kk.input_kk_r.value;

  // still_input is necessary for the while-loop
  still_input = true;

  while(still_input) {
    var userinput = String(kk_v + ": " + kk_r);

    // Append the userinput to a temp. storage (Array)
    temp = []
    temp.push(userinput);

    if (document.input_kk.finish_c_kk.onclick) {
      still_input = false;
    } else {}
  }

  //test
  alert(temp);
}

/*
function WriteIntxt(kk_v, kk_r) {
  
  var blob = new Blob([temp], { type: "text/plain;charset=utf-8"});

  saveAs(blob, "vocab.txt");
}
*/