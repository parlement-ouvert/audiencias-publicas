var questionSocket = createSocket("questions/stream/");

questionSocket.onmessage = function(message) {
  var data = JSON.parse(message.data);
  var exists = $(`[data-question-id=${data.id}]`);

  if (exists.length) {
    exists.replaceWith(data.html);
  } else {
    var questionsContainer = $('#questions');
    questionsContainer.append(data.html);
  }
  var newElement = $(`[data-question-id=${data.id}]`);
  newElement.on('click', upVote);
  var upvoteButton = newElement.find('.vote-block__upvote-button');
  var totalVotes = newElement.find('.vote-block__total-votes');

  if (HANDLER === newElement.data('question-author')) {
    upvoteButton.addClass('voted disabled');
    upvoteButton.attr('disabled', true);
    upvoteButton.html('Sua Pergunta');
    totalVotes.addClass('voted disabled');
  } else if ($.inArray(HANDLER, data.voteList) > -1) {
    upvoteButton.addClass('voted');
    upvoteButton.html('Apoiada por você');
    totalVotes.addClass('voted');
  } else {
    upvoteButton.removeClass('voted disabled');
    upvoteButton.removeAttr('disabled');
    upvoteButton.html('Votar Nesta Pergunta');
    totalVotes.removeClass('voted');
  }
};

$("#questionform").on("submit", function(event) {
  questionSocket.send(JSON.stringify({
    handler: HANDLER,
    question: $(this).find('input[name=question]').val(),
    is_vote: false,
  }));
  $("#question").val('').focus();
  return false;
});

function upVote() {
  var question_id = $(this).closest('.questions__item').data('question-id');
  questionSocket.send(JSON.stringify({
    handler: HANDLER,
    question: question_id,
    is_vote: true,
  }))
}

$(".question-vote").on('click', upVote);

questionSocket.onopen = function() { console.log("Connected to question socket"); }
questionSocket.onclose = function() { console.log("Disconnected to question socket"); }
