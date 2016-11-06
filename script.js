var users = [];
var money = [];
var goals = [];
var username = "";

document.addEventListener("DOMContentLoaded", function(event) { 
	console.log(localStorage.users);
  	if (localStorage.getItem("users") != null) {
	    users = JSON.parse(localStorage.getItem("users"));
	}
	if (localStorage.getItem("money") != null) {
	    money = JSON.parse(localStorage.getItem("money"));
	}
	if (localStorage.getItem("goals") != null) {
	    goals = JSON.parse(localStorage.getItem("goals"));
	}
});

function logIn(form) {
	if (localStorage.getItem("users") != null) {
	    users = JSON.parse(localStorage.getItem("users"));
	}
	match = false;
	for (var i = 0; i < users.length; i++) {
		if (users[i].email == form.email1.value && users[i].password == form.password1.value) {
			username = users[i].username;
			match = true;
			return true;
		}
	}
	alert("Wrong e-mail or password.");
	return false;
}
function signUp(form) {
	if (form.password2.value == form.password22.value) {
		var newUser = {
	      email: form.email2.value,
	      username: form.username.value,
	      password: form.password2.value
	    };
	    users.push(newUser);
	    updateDatabaseUsers(users);
	    username = users[i].username;
	    return true;
	}
	else {
		alert("Passwords don't match.");
		return false;
	}
} 

function updateDatabaseUsers(users) {
    localStorage.setItem("users", JSON.stringify(users));
}
function updateDatabaseMoney(money) {
    localStorage.setItem("money", JSON.stringify(money));
}
function updateDatabaseGoals(goals) {
    localStorage.setItem("goals", JSON.stringify(goals));
}