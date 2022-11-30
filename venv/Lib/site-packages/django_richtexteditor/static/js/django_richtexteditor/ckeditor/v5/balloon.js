let editors = [];

let config = {};
if (typeof RICHTEXTEDITOR_CONFIG !== 'undefined') config = RICHTEXTEDITOR_CONFIG;

document.addEventListener("DOMContentLoaded", () => {
  let _editors = document.querySelectorAll('.editor');
  for (let i=0; i < _editors.length; ++i) {
    BalloonEditor
      .create( _editors[i], config )
      .then( editor => {
        editors.push(editor);
      })
      .catch( err => {
        console.error( err.stack );
      });
  }
  window.editors = editors;
});