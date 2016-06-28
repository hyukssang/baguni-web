$(document).ready(function(){
	function checkFirstnameLength(){	
	var firstname = $('#input-signup-firstname');
	firstname.parent().removeClass('has-error');
	firstname.parent().removeClass('has-success');
	if(firstname.val() == ""){
		firstname.parent().addClass('has-error');
		firstname.next().text('Let us get to know you!');
	}	
	else{
		firstname.parent().addClass('has-success');
		firstname.next().text('FirstName - Check!');
	}
	return;
}
function checkLastnameLength(){
	var lastname = $('#input-signup-lastname');
	lastname.parent().removeClass('has-error');
	lastname.parent().removeClass('has-success');
	if(lastname.val() == ""){
		lastname.parent().addClass('has-error');
		lastname.next().text('Let us get to know you!');
	}	
	else{
		lastname.parent().addClass('has-success');
		lastname.next().text('LastName - Check!');
	}
	return;
}
function checkEmail(){
	var email = $('#input-signup-email');
	email.parent().removeClass('has-error');
	email.parent().removeClass('has-success');
	// var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	var re = /[^@]+@[^@]+\.[^@]/;
    if(!re.test(email.val())){
    	email.parent().addClass('has-error');
    	email.next().text('This is going to be your ID, so you better provide one!');
    }
    else if(email.val().length > 40){
    	email.parent().addClass('has-error');
    	email.next().text('Is your email really that long?');
    }
    else{
    	email.parent().addClass('has-success');
    	email.next().text('Email - Check!');
    }
    return;
}
function checkPassword(){
	var password = $('#input-signup-password');
	password.parent().removeClass('has-error');
	password.parent().removeClass('has-success');
	if(password.val().length < 8){
		password.parent().addClass('has-error');
    	password.next().text('Your password needs to be longer!');
	}
	else if(!(/^\w+$/.test(password.val()))){
		password.parent().addClass('has-error');
    	password.next().text('You may only contain letters, digits, and underscores');
	}
	else{
		var letterCheck = false;
		var numberCheck = false;
		for (var i = 0; i < password.val().length; i++){
			if(password.val()[i].match(/[A-Z|a-z]/i))
	            letterCheck=true;
	        if(!isNaN(password.val()[i]))
	            numberCheck=true;
		}
		if(!letterCheck || !numberCheck){
			password.parent().addClass('has-error');
	    	password.next().text('Passwords must contain at least one letter and one number');
		}
		else{
			password.parent().addClass('has-success');
			password.next().text('PW - Check!')	
		}
	}
	return;
}
function checkPhoneNum(){
	var phone = $('#input-signup-phone');
	phone.parent().removeClass('has-error');
	phone.parent().removeClass('has-success');
	var re = /[0-9]{10,11}/
	if(phone.val().length < 10 || phone.val().length > 11){
		phone.parent().addClass('has-error');
		phone.next().text('Too long or too short');
	}
	else if(!re.test(phone.val())){
		phone.parent().addClass('has-error');
		phone.next().text('Use only numbers');
	}
	else{
		phone.parent().addClass('has-success');
		phone.next().text('Phone - Check!');
	}
}
function beforeSubmit(e){
	e.preventDefault();
	if($('.has-success').length == 5){
		$('#form-signup')[0].submit();
	}
	else{
		alert("You are not ready to submit");
	}
}
$('#input-signup-firstname').change(checkFirstnameLength);
$('#input-signup-lastname').change(checkLastnameLength);
$('#input-signup-email').change(checkEmail);
$('#input-signup-phone').change(checkPhoneNum);
$('#input-signup-password').change(checkPassword);
$('#form-signup').submit(beforeSubmit);

});
