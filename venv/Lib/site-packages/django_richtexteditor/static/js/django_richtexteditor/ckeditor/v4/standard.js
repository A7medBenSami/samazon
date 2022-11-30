let editors = [];

let config = {};
if (typeof RICHTEXTEDITOR_CONFIG !== 'undefined') config = RICHTEXTEDITOR_CONFIG;

document.addEventListener("DOMContentLoaded", () => {
  let _editors = document.querySelectorAll('.editor');
  for (let i=0; i < _editors.length; ++i) {
    console.log(_editors[i].id)
    CKEDITOR.replace( document.querySelector( '#' + _editors[i].id ) );
  }
  window.editors = editors;
});