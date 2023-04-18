function createFolder() {
  var folderName = prompt('Enter a name for the folder:');
  if (folderName != null) {
      // Add folder to the DOM
      var folder = $('<div class="card"></div>').text(folderName);
      $('#folders').append(folder);

      // Add folder to the database
      $.ajax({
          url: '/create_folder',
          type: 'POST',
          data: {
              'folder_name': folderName
          },
          success: function(response) {
              console.log(response);
          }
      });
  }
}

function deleteFolder() {
  var folder = $(this).closest('.card');
  var folderName = folder.text().trim();

  // Remove folder from the DOM
  folder.remove();

  // Remove folder from the database
  $.ajax({
      url: '/delete_folder',
      type: 'POST',
      data: {
          'folder_name': folderName
      },
      success: function(response) {
          console.log(response);
      }
  });
}

function createFlashcard() {
  var cardFront = prompt('Enter the front of the flashcard:');
  var cardBack = prompt('Enter the back of the flashcard:');
  if (cardFront != null && cardBack != null) {
      // Add flashcard to the DOM
      var flashcard = $('<div class="card"></div>');
      var front = $('<div class="front"></div>').text(cardFront);
      var back = $('<div class="back"></div>').text(cardBack);
      flashcard.append(front);
      flashcard.append(back);
      $('#folders .card.active').append(flashcard);

      // Add flashcard to the database
      var folderName = $('#folders .card.active').text().trim();
      $.ajax({
          url: '/create_flashcard',
          type: 'POST',
          data: {
              'folder_name': folderName,
              'card_front': cardFront,
              'card_back': cardBack
          },
          success: function(response) {
              console.log(response);
          }
      });
  }
}

$('#create-folder').click(createFolder);

$('#folders').on('click', '.card .delete', deleteFolder);

$('#folders').on('click', '.card', function() {
  $(this).toggleClass('active').siblings().removeClass('active');
});

$('#create-flashcard').click(createFlashcard);

$('#folders').on('click', '.card .flashcard .edit', editFlashcard);

function editFlashcard() {
  var flashcard = $(this).closest('.flashcard');
  var cardFront = prompt('Enter the new front of the flashcard:', flashcard.find('.front').text());
  var cardBack = prompt('Enter the new back of the flashcard:', flashcard.find('.back').text());
  if (cardFront != null && cardBack != null) {
      // Update flashcard in the DOM
      flashcard.find('.front').text(cardFront);
      flashcard.find('.back').text(cardBack);

      // Update flashcard in the database
      var folderName = $('#folders .card.active').text().trim();
      var flashcardIndex = $('#folders .card.active .flashcard').index(flashcard);
      $.ajax({
          url: '/edit_flashcard',
          type: 'POST',
          data: {
              'folder_name': folderName,
              'flashcard_index': flashcardIndex,
              'card_front': cardFront,
              'card_back': cardBack
          },
          success: function(response) {
              console.log(response);
          }
      });
  }
}