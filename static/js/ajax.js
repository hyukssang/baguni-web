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
		url: '/api/v1/addBaguni',
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

// Adding a new Item
$('#btn-add-item').click(function(){
	var url = $('#input-item-url').val();
	var data = {
		"itemURL": url
	}
	var jsondata = JSON.stringify(data);
	console.log(jsondata);
	$.ajax({
		url: '/api/v1/addItem',
		type: 'POST',
		contentType: 'application/json; charset=UTF-8',
		data: jsondata,
		success:function(data){
			console.log('Item Added!');
		},
		error: function(xhr, status, errThrown){
			console.log(status);
		}
	});
});

