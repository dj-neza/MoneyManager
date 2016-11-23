var users = [];
var money = [];
var goals = [];
var currentUsername = "";

document.addEventListener("DOMContentLoaded", function(event) { 
  	if (localStorage.getItem("users") != null) {
	    users = JSON.parse(localStorage.getItem("users"));
	}
	if (localStorage.getItem("money") != null) {
	    money = JSON.parse(localStorage.getItem("money"));
	}
	if (localStorage.getItem("goals") != null) {
	    goals = JSON.parse(localStorage.getItem("goals"));
	}
	if (localStorage.getItem("currentUsername") != null) {
	    currentUsername = JSON.parse(localStorage.getItem("currentUsername"));
	}

	document.getElementById("toggle").onclick = function() {
		var d = document.getElementById("toggle");
		var d2 = document.querySelector('.menu_toggle');
		if(hasClass(d, 'acti')) {
	        d.className = d.className.replace(/\bacti\b/,'');
	        fadeOut(d2);
	    }
	    else {
	    	d.className += "acti";
	    	fadeIn(d2);
	    }
	}
	document.getElementById("toggle2").onclick = function() {
		var d = document.getElementById("toggle2");
		var d2 = document.querySelector('.menu_toggle2');
		if(hasClass(d, 'acti')) {
	        d.className = d.className.replace(/\bacti\b/,'');
	        fadeOut(d2);
	    }
	    else {
	    	d.className += "acti";
	    	fadeIn(d2);
	    }
	}
	document.getElementById("manW").onclick = function() {
		document.getElementById("manW").className = document.getElementById("manW").className.replace(/\bcolor_lvio\b/, "color_vio");
	}
	document.getElementById("manC").onclick = function() {
		document.getElementById("manC").className = document.getElementById("manC").className.replace(/\bcolor_lvio\b/, "color_vio");
	}
	document.getElementById("export").onclick = function() {
		document.getElementById("export").className = document.getElementById("export").className.replace(/\bcolor_lvio\b/, "color_vio");
	}
	document.getElementById("settings").onclick = function() {
		document.getElementById("settings").className = document.getElementById("settings").className.replace(/\bcolor_lvio\b/, "color_vio");
	}
	document.getElementById("profile").onclick = function() {
		document.getElementById("profile").className = document.getElementById("profile").className.replace(/\bcolor_lvio\b/, "color_vio");
	}
	document.getElementById("logout").onclick = function() {
		document.getElementById("logout").className = document.getElementById("logout").className.replace(/\bcolor_lvio\b/, "color_vio");
	}

	document.getElementById("exp").onclick = function() { gumbi("exp", "stat", "inc", "goal"); }
	document.getElementById("inc").onclick = function() { gumbi("inc", "exp", "stat", "goal"); }
	document.getElementById("goal").onclick = function() { gumbi("goal", "exp", "inc", "stat"); }
	document.getElementById("stat").onclick = function() { gumbi("stat", "exp", "inc", "goal"); }

});

function gumbi(id1, id2, id3, id4) {
	document.getElementById(id1).className = document.getElementById(id1).className.replace(/\bneaktivn\b/, "aktiven");
	document.getElementById(id2).className = document.getElementById(id2).className.replace(/\baktiven\b/, "neaktivn");
	document.getElementById(id3).className = document.getElementById(id3).className.replace(/\baktiven\b/, "neaktivn");
	document.getElementById(id4).className = document.getElementById(id4).className.replace(/\baktiven\b/, "neaktivn");
	document.getElementById(id1).style.height = "30px";
	document.getElementById(id2).style.height = "27px";
	document.getElementById(id3).style.height = "27px";
	document.getElementById(id4).style.height = "27px";
}

function hasClass(element, cls) {
    return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
}
function fadeOut(el){
  el.style.opacity = 1;

  (function fade() {
    if ((el.style.opacity -= .1) < 0) {
      el.style.display = 'none';
      el.classList.add('is-hidden');
    } else {
      requestAnimationFrame(fade);
    }
  })();
}

// fade in

function fadeIn(el, display){
  el.style.opacity = 0;
  el.style.display = display || "block";

  (function fade() {
    var val = parseFloat(el.style.opacity);
    if (!((val += .1) > 1)) {
      el.style.opacity = val;
      requestAnimationFrame(fade);
    }
  })();
}


function newTransaction() {

}
function newExpense() {

}
function newIncome() {

}

function newGoal() {

}
function addToGoal() {

}

function menu() {

}
function user() {

}
function updateBalance() {
	
}

function logIn(form) { //TODO - ne dela vec ker ni vezano na formo
	if (localStorage.getItem("users") != null) {
	    users = JSON.parse(localStorage.getItem("users"));
	}
	for (var i = 0; i < users.length; i++) {
		if (users[i].email == form.email1.value && users[i].password == form.password1.value) {
			currentUsername = users[i].username;
	    	updateDatabaseCurrent(currentUsername);
			return true;
		}
	}
	alert("Wrong e-mail or password.");
	return false;
}
function signUp(form) { //TODO - ne dela vec ker ni vezano na formo
	if (form.password2.value == form.password22.value) {
		var newUser = {
	      email: form.email2.value,
	      username: form.username.value,
	      password: form.password2.value
	    };
	    users.push(newUser);
	    updateDatabaseUsers(users);
	    currentUsername = users[i].username;
	    updateDatabaseCurrent(currentUsername);
	    return true;
	}
	else {
		alert("Passwords don't match.");
		return false;
	}
} 
function logOut() {
	var currentUser = ""
	updateDatabaseCurrent(currentUser);
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
function updateDatabaseCurrent(username) {
	localStorage.setItem("currentUsername", JSON.stringify(username));
}


function div_show(id) {
document.getElementById(id).style.display = "block";
}
//Function to Hide Popup
function div_hide(id){
document.getElementById(id).style.display = "none";
}