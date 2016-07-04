// Contains Javscript logic used at /bagunis

// Adding a new Item
$('#btn-add-item').click(function(){
	var itemURL = $('#input-item-url').val();
	var data = {
		"itemURL": itemURL
	}
	var jsondata = JSON.stringify(data);
	console.log(jsondata);
	$.ajax({
		url: window.location.pathname,
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