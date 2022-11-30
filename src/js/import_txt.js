const file = document.getElementById('import_txt');

file.addEventListener('change', function () {
  const reader = new FileReader();
  reader.onload = function (progressEvent) {
    console.log(this.result);

    let input = this.result;
    // check the type of the result
    let checkType = typeof this.result;
    console.log(checkType);
    // try to split it up, what worked :)
    let splitedup = input.split('\n');
    console.log(splitedup);
  };
  let full_file = reader.readAsText(this.files[0]);
  console.log(full_file);
});
