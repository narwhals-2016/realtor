function init_street_view(map_div,latitude, longitude) {
	// console.log(latitude, longitude);
	var var_location = new google.maps.LatLng(latitude,longitude);

	var var_mapoptions = {
		center: var_location,
		zoom: 14,
	};
	var var_map = new google.maps.Map(map_div, var_mapoptions);

	var var_marker = new google.maps.Marker({
		position: var_location,
		map: var_map,
		title:"Venice"
	});

  	var panorama = new google.maps.StreetViewPanorama(
      map_div, {
        position: var_location,
        pov: {
          heading: 34,
          pitch: 10
        }
    });
  	var_map.setStreetView(panorama);
	var_marker.setMap(var_map); 

}

function init_map(map_div,latitude, longitude) {
	// console.log(latitude, longitude);
	var var_location = new google.maps.LatLng(latitude,longitude);

	var var_mapoptions = {
		center: var_location,
		zoom: 14,
	};
	var var_map = new google.maps.Map(map_div, var_mapoptions);

	var var_marker = new google.maps.Marker({
		position: var_location,
		map: var_map,
	});
	
	var_marker.setMap(var_map); 
}


$(document).ready(function(){

	// street view 
	$(".street_view").on("click", function(event){
		event.preventDefault();
        var $map = $(this).parent().prev().children('.map-div');
        console.log("map", $map)

        var cards = $map.parents('.row').children();
        var $image_card = cards.first();
		$map.css('height',$image_card.css('height'));
		$map.addClass('image_height');

		var latitude = $map.data('lat');
		var longitude = $map.data('long');
		init_street_view($map[0], latitude, longitude);

	});

	// map view
	$(".map_view").on("click", function(event){
		event.preventDefault();
        var $map = $(this).parent().prev().children('.map-div');

        var cards = $map.parents('.row').children();
        var $image_card = cards.first();
		$map.css('height',$image_card.css('height'));
		$map.addClass('image_height');

		var latitude = $map.data('lat');
		var longitude = $map.data('long');
		init_map($map[0], latitude, longitude);

	});

});


