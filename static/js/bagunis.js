// Contains Javscript logic used at /bagunis

// loading screen
$('.container-items').css('height', window.innerHeight - 205);
$('.modal-body-nested').hide();

// ajax settings
$(document).ajaxStart(function(){
	$('#modal-btn-add').text('Parsing...').prop('disabled', true);
});
$(document).ajaxSuccess(function(){
	$('#modal-btn-add').text('Yes!').prop('disabled', false);
	
});
$(document).ajaxError(function(){
	$('#modal-btn-add').text('Parse').prop('disabled', false);
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
		$('<h6/>').append(selectTitle + ':')
	).append(' ').append(
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
$('#modal-btn-add').click(function(e){
	// Prepare the data to be sent to the server
	var itemURL = $('#modal-input-url').val();
	
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
			"price": $('.modal-body-nested dl dd:eq(2)').text(),
			"brandName": $('.modal-body-nested dl dd:eq(0)').text(),
			"itemName": $('.modal-body-nested dl dd:eq(1)').text(),
			"moreInfo": moreInfo
		}
	}
	var jsondata = JSON.stringify(data);
	console.log(jsondata);
	
	// For Parsing the url and retrieving item info
	if (step == 0){
		$.ajax({
			url: window.location.pathname,
			type: 'POST',
			contentType: 'application/json; charset=UTF-8',
			data: jsondata,
			dataType: 'JSON',
			success: function(data){	
				console.log(data.moreInfo);			
				$('#modal-input-url').prop('disabled', true);
				// Save the result so we don't have to parse once more
				$('.modal-body-nested img').attr('src', data.checkImage);
				$('.modal-body-nested dl dd:eq(0)').append(data.checkBrand);
				$('.modal-body-nested dl dd:eq(1)').append(data.checkName);
				$('.modal-body-nested dl dd:eq(2)').append(data.checkPrice);
				
				// key = size, color, etc
				// value = M, L, red, yellow, etc.
				$('.modal-body-nested').append($('<div/>', {'class': 'modal-nested-row'}));
				for (var key in data.moreInfo){
					// $('.modal-body-nested').append(addDropdown(key, data.moreInfo[key]));
					$('.modal-nested-row').append(
						createSelect(key, data.moreInfo[key])
					).append('  ');
					
				}
				$('.modal-nested-row').append(
					$('<button/>', {type: 'button', 'class': 'btn btn-black btn-xs', id: 'modal-nested-btn-add'}).append('ADD')
				);

				$('.modal-body-nested').show();
			},
			error: function(xhr, status, errThrown){
				console.log(status);
				$('.modal-body h5').first().text('Parsing failed. Please try again!');
			}
		});		
	}// For Actually inserting the info into the database
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

$('#modal-nested-btn-add').click(function(){
	if($('.modal-nested-row ul').length){
		$('.modal-body-nested').append(
			$('<div/>', {'class': 'modal-nested-row'}).append(
				$('<ul/>', {'class': 'modal-nested-list-items'})
			)
		);
	}
	// $('.modal-nested-list-items').append(function(){
	// 	var iteminfo = []
	// 	$('.modal-nested-row .selector').each(function(){
	// 		$(this).
	// 	});
	// })
});

// Upon closing the modal window
$('#modal-btn-add').next().click(function(e){
	$('.modal-body-nested').hide();
	// Reset parsed part
	$('.modal-body-nested img').attr('src', '');
	$('.modal-body-nested dd').text('');
	$('.modal-nested-row').remove();
	$('.selector').remove();
	// Reset footer buttons
	$('#modal-btn-add').text('Parse');
	$('#modal-input-url').prop('disabled', false).val('');
});













