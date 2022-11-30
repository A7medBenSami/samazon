let editors = [];

let config = {};
if (typeof RICHTEXTEDITOR_CONFIG !== 'undefined') config = RICHTEXTEDITOR_CONFIG;

document.addEventListener("DOMContentLoaded", () => {
  let _editors = document.querySelectorAll('.editor');
  for (let i=0; i < _editors.length; ++i) {

  DecoupledEditor
    .create( _editors[i], config )
    .then( editor => {
      const toolbarContainer = document.querySelector( '.toolbar-container' );
      toolbarContainer.appendChild( editor.ui.view.toolbar.element );
      editors.push(editor);
    })
    .catch( err => {
      console.error( err.stack );
    });
  }
  window.editors = editors;
});
