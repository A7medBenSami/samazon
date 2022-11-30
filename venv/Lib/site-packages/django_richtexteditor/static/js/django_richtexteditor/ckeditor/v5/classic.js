let config = {};
if (typeof RICHTEXTEDITOR_CONFIG !== 'undefined') config = RICHTEXTEDITOR_CONFIG;

document.addEventListener("DOMContentLoaded", () => {

  let textareas = document.querySelectorAll('.editor');

  for (let i=0; i < textareas.length; ++i) {

    setTimeout(function() {
      ClassicEditor
        .create( textareas[i], config )
        .then( editor => {
           // console.log( editor );
        })
        .catch( err => {
          console.error( err.stack );
        });
    }, 1000);
  }

});
