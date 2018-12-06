$(document).ready( function () {

$.getJSON('https://ipinfo.io/json', function(response) {

		$.post('/', function(){
			// console.log(JSON.stringify(response, null, 2));
			// alert(response.ip);
			// alert(response.loc);
			ip_val=response.ip;
			loc_value=response.loc;
			$("#ip").prop("value",response.ip);
			$("#loc").prop("value",response.loc);
			
			return response;
			})
	
	})
})