#html/javascript page to get user input
#function to get the URL list from html form & save to table
#name

#This function takes the inputs from the javascript form and writes them to a .txt file named by the uwnetid of the TA
#list for urls
#HTML form
<form name="url_list" action"/bin/retrieve.py" method="POST">
	<div id="dynamicInput">
		Entry 1: <input type="text" name="urls[]">
	</div>
	<input type="button" value"Add another text input" onClick="addInput('dynamicInput');">
</form>
#Javascript
var counter = 1;
var limit = 25;

function addInput(divName) {
	if (counter == limit) {
		alert("Courses are capped at 23. Do you have this many students?");
	}
	else {
		var newdiv = document.createElement('div');
		newdiv.innerHTML = "Entry " + (counter + 1) + ": " + "<input type = 'text' name = 'urls[]'>";
		document.getElementById(divName).appendChild(newdiv);
		counter++;
	}

#php script
$myInputs = $_POST["urls"];
foreach($urls as $url) {
	$cleanedurl = 




urls = []
filename = 
def write_url(filename):
	txt = open(filename, 'w')
	for url in urls:
		txt.write(url)
		text.write("\n")
	txt.close()
	print "%r has been written to disk." % filename




	

	

