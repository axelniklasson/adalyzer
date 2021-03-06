function initMap() {
    var cords = {lat: 57.68, lng: 11.993};

    var map = new google.maps.Map(document.getElementById('location-map'), {
        zoom: 11,
        center: cords
    });

    var images = [{
		url: 'img/persona-map-1.png',
		// This marker is 20 pixels wide by 32 pixels high.
		size: new google.maps.Size(30, 33),
		// The origin for this image is (0, 0).
		origin: new google.maps.Point(0, 0),
		// The anchor for this image is the base of the flagpole at (0, 32).
		anchor: new google.maps.Point(0, 28)
		},
		{
		url: 'img/persona-map-2.png',
		// This marker is 20 pixels wide by 32 pixels high.
		size: new google.maps.Size(30, 33),
		// The origin for this image is (0, 0).
		origin: new google.maps.Point(0, 0),
		// The anchor for this image is the base of the flagpole at (0, 32).
		anchor: new google.maps.Point(0, 28)
		},
		{url: 'img/persona-map-3.png',
		// This marker is 20 pixels wide by 32 pixels high.
		size: new google.maps.Size(30, 33),
		// The origin for this image is (0, 0).
		origin: new google.maps.Point(0, 0),
		// The anchor for this image is the base of the flagpole at (0, 32).
		anchor: new google.maps.Point(0, 28)
		},
		{url: 'img/persona-map-4.png',
		// This marker is 20 pixels wide by 32 pixels high.
		size: new google.maps.Size(30, 33),
		// The origin for this image is (0, 0).
		origin: new google.maps.Point(0, 0),
		// The anchor for this image is the base of the flagpole at (0, 32).
		anchor: new google.maps.Point(0, 28)
		}];

  	var cars = new google.maps.Marker({
    	position: {lat: 57.68, lng: 11.993},
    	map: map,
    	icon: images[0],
	});
}