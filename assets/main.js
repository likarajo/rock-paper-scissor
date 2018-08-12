//Using JQuery

$(document).ready(function() {
  $('#demoLink').click(function() {
    $('#home').animate({ opacity: "-=1" }, 500, function() { $('#home').hide(); });
    $('#demo').animate({ opacity: "+=1" }, 500, function() { $('#demo').show(); });
    return false;
  });
});


$(document).ready(function() {
  $('#homeLink').click(function() {
    $('#demo').animate({ opacity: "-=1" }, 500, function() { $('#demo').hide(); });
    $('#home').animate({ opacity: "+=1" }, 500, function() { $('#home').show(); });
    return false;
  });
});
