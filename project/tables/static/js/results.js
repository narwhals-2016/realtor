function init_map(map_div,latitude, longitude) {
	console.log(latitude, longitude);
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

$(document).ready(function(){

	$(".bold_hover").on("click", function(event){
		event.preventDefault();
		// console.log('inside bold_hover clicked')
        var $map = $(this).parent();
        var cards = $map.parents('.row').children();
        var $image_card = cards.first();

		$map.css('height',$image_card.css('height'));
		// $('#map-div').css('')
		var latitude = $map.data('lat');
		var longitude = $map.data('long');
		init_map($map[0], latitude, longitude);

	});
});