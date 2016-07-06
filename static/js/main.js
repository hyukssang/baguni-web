// Contains Javscript logic used at /main

// var bgHeight = $('.bg').css('height');
// $('.container-bagunis').css('height', window.innerHeight - bgHeight - 165);

// Adding a new Baguni
$('#btn-add-baguni').click(function(){
	var baguniName = $('#input-baguni-name').val();
	var baguniColor = $('input[type="radio"]:checked').val();
	var data = {
		"baguniName": baguniName,
		"baguniColor": baguniColor
	}
	var jsondata = JSON.stringify(data);
	console.log(jsondata);
	$.ajax({
		url: window.location.pathname,
		type: 'POST',
		contentType: 'application/json; charset=UTF-8',
		data: jsondata,
		success: function(data){
			location.reload();
		},
		error: function(xhr, status, errThrown){
			console.log(status);
		}
	});
});