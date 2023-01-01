const LINE_BREAKER = '\n';
const LINE_SPLITTER = ": ";


const onFileLoad = (progressEvent) => {
  const input = this.result;
  if (typeof input !== 'string') throw new Error("Kein string");

  // Try to split it up, what worked :)
  const importedKKs = input.split('\n').map(line => line.split(LINE_SPLITTER))

  if (file_name in localStorage) {
    for (let index = 0; index < imported_kk.length; index++) {
      let saved_element = localStorage.getItem(file_name);
      const element = `[${imported_kk[index]}]`;
    }
  }
};

const readFileAsync = (file) => new Promise((resolve, reject) => {
  const reader = new FileReader();
  reader.onload = () => resolve(reader.result);
  reader.onerror = reject;
  reader.readAsText(file);
})

const parseFile = (content) => content.split(LINE_BREAKER).map(line => line.split(LINE_SPLITTER))

const importParsedKKs = (categoryName, cards = []) => {
  try {
    const categoryExists = localStorage.getItem(categoryName);
    if (!categoryExists) {
      localStorage.setItem(category, JSON.stringify(cards));
      return;
    }
    const oldSet = JSON.parse(categoryExists)
    

  } catch (err) {
    console.error(err)
    // TODO: Add handling if an error on JSON parse happends
  }

}

const processFile = async () => {
  const file = importInput.files[0]
  if (!file) throw new Error('Kein Datei')
  const fileContent = await readFileAsync(file)
  const fileName = file.name.replace('.txt', '');
  const parsed = parseFile(fileContent)
  importParsedKKs(fileName, parsed)
}

const importInput = document.getElementById('import_txt');
importInput.addEventListener('change', processFile);
