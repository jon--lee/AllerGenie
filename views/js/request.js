console.log("hello world from home.js");

$("button").click(function(){
	var searchTerm = $('#searchBox').val();
	var loc = $('#locBox').val();
	var allergy = $('#allergyBox').val();
	console.log(searchTerm);
	console.log(loc);
	$.ajax({
		type: "POST",
		url: "../search/",
		dataType: 'json',
		data: JSON.stringify({ "searchTerm": searchTerm, "loc": loc })
	}).done(function(data){
		alert("received data!");
		//var array = data.split(',');
		console.log(data[0]);
		var results = JSON.stringify(data);
		console.log(results);
		var results = results.split(',');
		var html = "";
		for(result in data)
		{
			html += "<a href='/request/?url=" + data[result] + "&allergy=" + allergy + "&searchTerm=" + searchTerm + "&loc=" + loc + "'>" + data[result] + "</a>";
			html += "<br>";
		}
		console.log(html);
		$('#printable').html(html);

		
		//console.log("" + JSON.stringify(data['data']));
	});
});


