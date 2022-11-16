// when a file is chosen in the input field, then the function(s) below will be executed

document.getElementById('import_txt').onchange = function(){
  var file = this.files[0];
  var reader = new FileReader();

  reader.onload = function(progressEvent) {
    var fileContentArray = this.result.split(/\r\n|\n/);
    for(var line = 0; line < lines.length-1; line++){
      console.log(line + " --> "+ lines[line]);
    }
  };
  reader.readAsText(file);
};
