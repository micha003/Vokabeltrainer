const file = document.getElementById('import_txt');

file.addEventListener('change', function () {
  const reader = new FileReader();
  reader.onload = function (progressEvent) {
    console.log(this.result);
  };
  const full_file = reader.readAsText(this.files[0]);
  console.log(full_file);
});
