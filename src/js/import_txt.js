const file = document.getElementById('import_txt');
let file_name = file.files[0].name.replace('.txt', '');

console.log(file_name);

file.addEventListener('change', function () {
  const reader = new FileReader();
  reader.onload = function (progressEvent) {
    console.log(this.result);

    let input = this.result;
    // check the type of the result
    const checkType = typeof this.result;
    console.log(checkType);
    // try to split it up, what worked :)
    let imported_kk = input.split('\n');
    console.log(imported_kk);

    if (file_name in localStorage) {
      for (let index = 0; index < imported_kk.length; index++) {
        let saved_element = localStorage.getItem(file_name);
        const element = `[${imported_kk[index]}]`;
      }
    }
  };
  let full_file = reader.readAsText(this.files[0]);
});
