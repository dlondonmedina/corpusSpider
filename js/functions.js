var counter = 1;
var limit = 25;

function addInput(divName) {
	if (counter == limit) {
		alert("Courses are capped at 23. Do you have this many students?");
	}
	else {
		var newdiv = document.createElement('div');
		newdiv.innerHTML = "Entry " + (counter + 1) + ": " + "<input type = 'text' name = 'urls'>";
		document.getElementById(divName).appendChild(newdiv);
		counter++;
	}