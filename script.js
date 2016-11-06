var users = [];
var money = [];
var goals = [];

document.addEventListener("DOMContentLoaded", function(event) { 
  	if (localStorage.getItem("users") != null) {
	    users = JSON.parse(localStorage.getItem("users"));
	    console.log(users);
	}
	console.log(users);
	if (localStorage.getItem("money") != null) {
	    money = JSON.parse(localStorage.getItem("money"));
	}
	if (localStorage.getItem("goals") != null) {
	    goals = JSON.parse(localStorage.getItem("goals"));
	}
});

function logIn(form) {

}
function signUp(form) {
	console.log(form.password2.value);
	console.log(form.password22.value);
	if (form.password2.value == form.password22.value) {
		var newUser = {
	      email: form.email2.value,
	      username: form.userName.value,
	      password: form.password2.value
	    };
	    users.push(newUser);
	    updateCommentDatabaseUsers();
	    console.log("lala");
	    console.log(users);
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