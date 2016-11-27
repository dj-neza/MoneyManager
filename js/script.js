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

	var pageName = (function () {
        var a = window.location.href,
            b = a.lastIndexOf("/");
        return a.substr(b + 1);
    }());
    if (pageName[0] == "a") {
    	document.getElementById("managing").onchange = function() {
			var val = document.getElementById("managing").options[document.getElementById("managing").selectedIndex].value;
			if (val == 1) {
		    	if(hasClass(document.getElementById("manex"), 'neviden')) {
		        	document.getElementById("manex").className = document.getElementById("manex").className.replace(/\bneviden\b/,'');
		    	}
		    	if(!hasClass(document.getElementById("manin"), 'neviden')) {
		        	document.getElementById("manin").className += "neviden";
		    	}
		    }
		    else if (val == 2) {
		    	if(hasClass(document.getElementById("manin"), 'neviden')) {
		        	document.getElementById("manin").className = document.getElementById("manin").className.replace(/\bneviden\b/,'');
		    	}
		    	if(!hasClass(document.getElementById("manex"), 'neviden')) {
		        	document.getElementById("manex").className += "neviden";
		    	}
		    }
		}
		document.getElementById("transactions").onchange = function() {
			var val = document.getElementById("transactions").options[document.getElementById("transactions").selectedIndex].value;
			if (val == 1) {
				if(hasClass(document.getElementById("to"), 'neviden')) {
		        	document.getElementById("to").className = document.getElementById("to").className.replace(/\bneviden\b/,'');
		    	}
		    	if(!hasClass(document.getElementById("excat"), 'neviden')) {
		        	document.getElementById("excat").className += "neviden";
		        	document.getElementById("loan1").className += "neviden";
		        	document.getElementById("loan2").className += "neviden";
		    	}
		    	if(!hasClass(document.getElementById("incat"), 'neviden')) {
		        	document.getElementById("incat").className += "neviden";
		        	document.getElementById("debt1").className += "neviden";
		        	document.getElementById("debt2").className += "neviden";
		    	}
			}
			else if (val == 2) {
				if(hasClass(document.getElementById("excat"), 'neviden')) {
		        	document.getElementById("excat").className = document.getElementById("excat").className.replace(/\bneviden\b/,'');
		        	document.getElementById("loan1").className = document.getElementById("loan1").className.replace(/\bneviden\b/,'');
		        	document.getElementById("loan2").className = document.getElementById("loan2").className.replace(/\bneviden\b/,'');
		    	}
		    	if(!hasClass(document.getElementById("to"), 'neviden')) {
		        	document.getElementById("to").className += "neviden";
		    	}
		    	if(!hasClass(document.getElementById("incat"), 'neviden')) {
		        	document.getElementById("incat").className += "neviden";
		        	document.getElementById("debt1").className += "neviden";
		        	document.getElementById("debt2").className += "neviden";
		    	}
			}
			else if (val == 3) {
				if(hasClass(document.getElementById("incat"), 'neviden')) {
		        	document.getElementById("incat").className = document.getElementById("incat").className.replace(/\bneviden\b/,'');
		        	document.getElementById("debt1").className = document.getElementById("debt1").className.replace(/\bneviden\b/,'');
		        	document.getElementById("debt2").className = document.getElementById("debt2").className.replace(/\bneviden\b/,'');
		    	}
		    	if(!hasClass(document.getElementById("to"), 'neviden')) {
		        	document.getElementById("to").className += "neviden";
		    	}
		    	if(!hasClass(document.getElementById("excat"), 'neviden')) {
		        	document.getElementById("excat").className += "neviden";
		        	document.getElementById("loan1").className += "neviden";
		        	document.getElementById("loan2").className += "neviden";
		    	}
			}
		}
		document.getElementById("toggle").onclick = function() {
			var d = document.getElementById("toggle");
			var d2 = document.querySelector('.menu_toggle');
			if(hasClass(d, 'acti')) {
		        d.className = d.className.replace(/\bacti\b/,'');
		        fadeOut(d2);
		    }
		    else {
		    	d.className += " acti";
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
		    	d.className += " acti";
		    	fadeIn(d2);
		    }
		}

		document.getElementById("exp").onclick = function() { 
			gumbi("exp", "stat", "inc", "goal"); 
			openTab("expensecontent", "statscontent", "incomecontent", "goalscontent");
		}
		document.getElementById("inc").onclick = function() { 
			gumbi("inc", "exp", "stat", "goal"); 
			openTab("incomecontent", "expensecontent", "statscontent", "goalscontent");
		}
		document.getElementById("goal").onclick = function() { 
			gumbi("goal", "exp", "inc", "stat"); 
			openTab("goalscontent", "expensecontent", "incomecontent", "statscontent");
		}
		document.getElementById("stat").onclick = function() { 
			gumbi("stat", "exp", "inc", "goal"); 
			openTab("statscontent", "expensecontent", "incomecontent", "goalscontent");
		}
    }
    else if (pageName[0] == "i") {
    	document.getElementById("login_button").onclick = function() {
			logIn("login");
		}
		document.getElementById("signup_button").onclick = function() {
			signUp("signup");
		}
    }
});

function gumbi(id1, id2, id3, id4) {
	document.getElementById(id1).className = document.getElementById(id1).className.replace(/\bneaktivn\b/, "aktiven");
	document.getElementById(id2).className = document.getElementById(id2).className.replace(/\baktiven\b/, "neaktivn");
	document.getElementById(id3).className = document.getElementById(id3).className.replace(/\baktiven\b/, "neaktivn");
	document.getElementById(id4).className = document.getElementById(id4).className.replace(/\baktiven\b/, "neaktivn");
}
function openTab(id1, id2, id3, id4) {
	if (hasClass(document.getElementById(id1), 'neviden')) {
		document.getElementById(id1).className = document.getElementById(id1).className.replace(/\bneviden\b/,'');
	}
	if (!hasClass(document.getElementById(id2), 'neviden')) {
		document.getElementById(id2).className += " neviden";
	}
	if (!hasClass(document.getElementById(id3), 'neviden')) {
		document.getElementById(id3).className += " neviden";
	}
	if (!hasClass(document.getElementById(id4), 'neviden')) {
		document.getElementById(id4).className += " neviden";
	}
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

function logIn(formid) { //TODO - ne dela vec ker ni vezano na formo
	var form = document.getElementById(formid);
	if (localStorage.getItem("users") != null) {
	    users = JSON.parse(localStorage.getItem("users"));
	}
	for (var i = 0; i < users.length; i++) {
		if (users[i].email == form.email1.value && users[i].password == form.password1.value) {
			currentUsername = users[i].username;
	    	updateDatabaseCurrent(currentUsername);
			window.location.href = "app.html";
		}
	}
	if (validateEmail(form.email1.value) == true) {
		window.location.href = "app.html";
	}
	else {
		alert("Enter a valid email");
	}
	//alert("Wrong e-mail or password.");
}
function signUp(formid) { //TODO - ne dela vec ker ni vezano na formo
	var form = document.getElementById(formid);
	if (form.password2.value == form.password22.value) {
		if (validateEmail(form.email2.value) == true) {
			var newUser = {
		      email: form.email2.value,
		      username: form.username.value,
		      password: form.password2.value
		    };
		    users.push(newUser);
		    updateDatabaseUsers(users);
		    currentUsername = form.username.value;
		    updateDatabaseCurrent(currentUsername);
		    window.location.href = "app.html";
		}
		else {
			alert("Enter a valid email.");
		}
	}
	else {
		alert("Passwords don't match.");
	}
} 
function logOut() {
	var currentUser = "";
	updateDatabaseCurrent(currentUser);
}
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
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
function div_hide(id){
	document.getElementById(id).style.display = "none";
}

/* FUNCIONALITY STUFF
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
*/