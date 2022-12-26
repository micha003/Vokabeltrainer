'use strict';

const EXPORT_FILE_TYPE = 'text/plain;charset=utf-8';

/**
 * Start downloading of your text file
 * @param {string} filename - File's name
 * @param {string} text - Content
 */
const download = (filename, text) => {
  // Create link DOM element
  const element = document.createElement('a');
  // Set content to download as url encoded string
  element.setAttribute('href', `data:${EXPORT_FILE_TYPE},${encodeURIComponent(text)}`);
  // Mark the file to be downloaded, not opened, when you click on it
  element.setAttribute('download', filename);
  // Add style to not be shown, append to the DOM
  element.style.display = 'none';
  document.body.appendChild(element);
  // Force click on it an delete the element
  element.click();
  document.body.removeChild(element);
};

/**
 * Get value of an input with addition validation
 * @param {string} inputId - ID of the input
 * @param {boolean} [ignoreCheck=false] - Whether to ignore the validation of input's value
 * @returns {(string|null)} - String on success, null if it did not pass the validation
 */
const getStringInput = (inputId, ignoreCheck = false) => {
  const { value } = document.getElementById(inputId);
  const isValid = typeof value === 'string' && value.length > 0;
  return isValid || ignoreCheck ? value : null;
};

const setInputValue = (inputId, value) => {
  const input = document.getElementById(inputId);
  input.value = value;
  return true;
};

const createLernset = (name) => {
  const shouldCreate = confirm('Es gibt noch kein solches Lernset. Wollen Sie es erstellen?');
  if (!shouldCreate) return false;
  localStorage.setItem(name, '[]');
  return true;
};

const getChosenSetName = () => {
  const inputId = 'choose_set';
  const chosenSetName = getStringInput(inputId);
  if (!chosenSetName) {
    const newName = prompt('Bitte geben Sie einen Namen für das Lernset ein:');
    setInputValue(inputId, newName);
    return getChosenSetName();
  }
  return chosenSetName;
}

const pushKK = () => {
  getChosenSetName();
  try {
    const inputsList = ['kk_v', 'kk_r'];
    const userInput = inputsList.map((inputId) => getStringInput(inputId));
    const isAllValid = userInput.every((val) => !!val);
    if (!isAllValid) throw new Error('Die Eingabe ist nicht vollständig');
    saveToStorage(userInput);
  } catch (err) {
    console.error(err);
    alert(err.message);
  }
}

const getFromStorage = (id) => {
  try {
    const rawItem = localStorage.getItem(id);
    return JSON.parse(rawItem);
  } catch (err) {
    console.error(err);
  }
};

const prepareForExport = (body) => body.map((card) => card.join(': ')).join('\n');

const exportSet = () => {
  try {
    // takes the value of an input field and set it as the file name
    const name = getChosenSetName();
    const body = getFromStorage(name);
    if (body.length === 0) throw new Error('Sie müssen zuerst mindestens ein Wort hinzufügen');
    // Saves the .txt-file
    const normalizedName = name.toLowerCase().replaceAll(' ', '-');
    download(`${normalizedName}.txt`, prepareForExport(body));
  } catch (err) {
    console.error(err);
    alert(err.message);
  }
}

const clearStorage = () => localStorage.clear();

const saveToStorage = (userInput) => {
  const name = getChosenSetName();
  let setBody = getFromStorage(name);
  if (!setBody) {
    const isCreated = createLernset(name);
    if (!isCreated) return null;
    setBody = [];
  }
  setBody.push(userInput);
  localStorage.setItem(name, JSON.stringify(setBody));
}
