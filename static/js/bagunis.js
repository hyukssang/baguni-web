// Contains Javscript logic used at /bagunis


$('.container-items').css('height', window.innerHeight - 205);
$('.modal-body-nested').hide();

$(document).ajaxStart(function(){
	$('#btn-add-item').text('Parsing...').prop('disabled', true);
});
$(document).ajaxSuccess(function(){
	$('#btn-add-item').text('Yes!').prop('disabled', false);
	
});
$(document).ajaxError(function(){
	$('#btn-add-item').text('Parse').prop('disabled', false);
});

// Creates a new dropdown button and menu
// function addDropdown(menuTitle, menuElems){
// 	var dropdown = $('<div/>', {'class': 'dropdown'}).append(
// 		$('<button/>', {
// 			'class': 'btn btn-default dropdown-toggle',
// 			type: 'button',
// 			'data-toggle': 'dropdown',
// 			'aria-haspopup': 'true',
// 			'aria-expanded': 'true'
// 		}).append(menuTitle).append(
// 			$('<span/>',{
// 				'class': 'caret'
// 			})
// 		)
// 	).append(
// 		$('<ul/>', {
// 			'class': 'dropdown-menu'
// 		}).append(function(){
// 			var elements = $();
// 			for(var i = 0; i < menuElems.length; i++){
// 				elements = elements.add($('<li/>').append($('<a/>', {href: '#'}).append(menuElems[i])));
// 			}
// 			return elements;
// 		})
// 	)
// 	return dropdown;
// }

// Creates a new select tag
function createSelect(selectTitle, selectElems){
	var select = $('<div/>', {'class': 'selector'}).append(
		$('<p/>').append(selectTitle)
	).append(
		$('<select/>').append(function(){
			var elements = $();
			for(var i = 0; i < selectElems.length; i++){
				elements = elements.add($('<option/>', {value: selectElems[i]}).append(selectElems[i]));
			}
			return elements;
		})
	);
	return select;
}

// Adding a new Item
$('#btn-add-item').click(function(e){
	// Prepare the data to be sent to the server
	var itemURL = $('#input-item-url').val();
	
	var step;
	if($(e.target).text() == 'Parse'){
		step = 0;
		var data = {
			"itemURL": itemURL, 
			"step": step,
		}
	}
	else{
		step = 1;
		moreInfo = "";
		for(var i = 0; i < $('select').length; i++){
			moreInfo = moreInfo.concat("/", $('.selector:eq('+i+') p').text(), ": ", $('select:eq('+i+') option:selected').val());
		}

		var data = {
			"itemURL": itemURL,
			"step": step,
			"imageURL": $('.modal-body-nested img').attr('src'),
			"price": $('.modal-body-nested p>span').text(),
			"brandName": $('.modal-body-nested h6:eq(0)>span').text(),
			"itemName": $('.modal-body-nested h6:eq(1)>span').text(),
			"moreInfo": moreInfo
		}
	}
	var jsondata = JSON.stringify(data);
	console.log(jsondata);
	
	if (step == 0){
		$.ajax({
			url: window.location.pathname,
			type: 'POST',
			contentType: 'application/json; charset=UTF-8',
			data: jsondata,
			dataType: 'JSON',
			success: function(data){				
				$('#input-item-url').prop('disabled', true);
				// Save the result so we don't have to parse once more
				$('.modal-body-nested img').attr('src', data.checkImage);
				$('.modal-body-nested h6:eq(0)>span').append(data.checkBrand);
				$('.modal-body-nested h6:eq(1)>span').append(data.checkName);
				$('.modal-body-nested p:eq(0)>span').append(data.checkPrice);
				
				// key = size, color, etc
				// value = M, L, red, yellow, etc.
				for (var key in data.moreInfo){
					// $('.modal-body-nested').append(addDropdown(key, data.moreInfo[key]));
					$('.modal-body-nested').append(createSelect(key, data.moreInfo[key]));
				}

				$('.modal-body-nested').show();
			},
			error: function(xhr, status, errThrown){
				console.log(status);
				$('.modal-body h5').first().text('Parsing failed. Please try again!');
			}
		});		
	}
	else{
		$.ajax({
			url: window.location.pathname,
			type: 'POST',
			contentType: 'application/json; charset=UTF-8',
			data: jsondata,
			success: function(){
				location.reload();
			},
			error: function(xhr, status, errThrown){
				console.log(status);
				$('.modal-body h5').first().text('Insertion failed. Please try again!');
			}
		});
	}
	
});

$('#btn-add-item').next().click(function(e){
	$('.modal-body-nested').hide();
	$('.modal-body-nested img').attr('src', '');
	$('.modal-body-nested h6:eq(0)>span').text('');
	$('.modal-body-nested h6:eq(1)>span').text('');
	$('.modal-body-nested p:eq(0)>span').text('');
	$('.selector').remove();
	$('#btn-add-item').text('Parse');
	$('#input-item-url').prop('disabled', false).val('');
});













