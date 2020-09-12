function selected_client(){
	// should be got from db.
	var dummy_lashes_list = [
		'8-9-10-11B-11-12-11-10C',
		'8-9-11-12-13-12',
		'8-9-10-11-10-9',
		'8-9-10-11-12-13-12-11-10-9-8'
	]
	
	var sc = document.getElementById("client_list").value;
	
	
	document.getElementById("client").innerHTML = dummy_lashes_list[sc];
}

function add_visit(){
	// should be stored in db
	
	var e = document.getElementById("client_list");
	var sc = e.options[e.selectedIndex].text;
	var today = new Date()
	var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
	var notes = document.getElementById("lash").value;
	
	// should be stored in db
	document.getElementById("client").innerHTML = sc
		+ ' data:' + date + ' notes:' + notes;
}

function readTextFile(file)
{
	    var rawFile = new XMLHttpRequest();
	    rawFile.open("GET", file, false);
	    rawFile.onreadystatechange = function ()
	    {
		    if(rawFile.readyState === 4)
			{
				if(rawFile.status === 200 || rawFile.status == 0)
				{
					var allText = rawFile.responseText;
					//alert(allText);
				}
			}
		}
	rawFile.send(null);
	return allText;
}

function callClients(){
	var ip = readTextFile("ip.txt");
	document.getElementById("client").innerHTML = ip;
	
	//$.get( "http://" + ip + ":5000/api/v1.0/clients", function( data ) {
	        //$('#clients').html(data);
	//	document.getElementById("client").innerHTML = data;
	//});
}

