$('#btn-add-baguni').click(function(){
	var value = $('#input-baguni-name').val();
	var data = {"baguniName": value}
	var jsondata = JSON.stringify(data);
	console.log(jsondata);
	$.ajax({
		url: '/api/v1/addBaguni',
		type: 'POST',
		contentType: 'application/json; charset=UTF-8',
		data: jsondata,
		dataType: 'json',
		success: function(data){
			console.log(data);
		},
		error: function(xhr, status, errThrown){
			console.log(status);
		}
	});
});