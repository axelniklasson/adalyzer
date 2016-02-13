var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices']);

adalyzerControllers.controller('MainController', ['$scope', 'BackendService', function($scope, BackendService) {
}]);

adalyzerControllers.controller('MapController', ['$scope', 'BackendService', function($scope, BackendService, NgMap) {
	$scope.title = 'Key points';

	// initialize an array with markers
	var markers = [];

	// car image
	var image = {
		url: 'img/car.png',
		// This marker is 20 pixels wide by 32 pixels high.
		size: new google.maps.Size(50, 50),
		// The origin for this image is (0, 0).
		origin: new google.maps.Point(0, 0),
		// The anchor for this image is the base of the flagpole at (0, 32).
		anchor: new google.maps.Point(0, 0)
	};

	// mockup car JSON
	var cars = [
		{
			'id':'1',
			'lat':'57.60',
			'lng':'12'
		},
		{
			'id':'2',
			'lat':'58.00',
			'lng':'12.2'
		},
		{
			'id':'3',
			'lat':'58.1',
			'lng':'12.1'
		}
	];

	// function that runs when the map has initialized
	$scope.$on('mapInitialized', function(event, map) {
		$scope.map = map;
		console.log("Map loaded. Ready to handle new markers");
		for(i = 0; i < cars.length; i++){
			add_markers(cars[i].lat, cars[i].lng);	
		}

		// Move a marker to a new position
		//setTimeout(function() { var latlng = new google.maps.LatLng(57.68, 12); markers[0].setPosition(latlng); }, 5000);
	});

	setTimeout(function() {
		BackendService.history().success(function(data) {
			var latLngObj = data["positioning_system"]["location"];
			var latlng = new google.maps.LatLng(latLngObj['lat'], latLngObj['lng']);
			markers[0].setPosition(latlng);
		}).error(function() {
			console.log("count: error");
		});
	}, 1000);

	// function to add a new marker using img_id which is a persona id,
	// lat and lng of the car / persona
	function add_markers(lat, lng){
		var marker = new google.maps.Marker({
			title: "car",
			icon: image
		});

		var latlng = new google.maps.LatLng(lat, lng);
		marker.setPosition(latlng);
		marker.setMap($scope.map);

		markers.push(marker);			
	}


}]);

/* Controllers fetching data for the different personas */
adalyzerControllers.controller('PersonasController', ['$scope', function($scope) {
	$scope.title = 'Personas';

	var data = [
		{
			'name': 'John Doe',
			'age': '20 y/o',
			'interests': []
		},
		{
			'name': 'Jane Doe',
			'age': '20 y/o',
			'interests': []
		},
		{
			'name': 'Steve Jobs',
			'age': '20 y/o',
			'interests': []
		},
		{
			'name': 'Steve Wozniak',
			'age': '20 y/o',
			'interests': []
		},
	];

	// BackendService.personas().success(function(data) {
	// 	$scope.personas = data;
	// }).error(function() {
	// 	console.log("count: error");
	// });

	angular.forEach(data, function(value, key) {
		value.img = 'img/persona-' + (key + 1) + '.png';
	});
	
	$scope.personas = data;
}]);


/* Controller for the Mapping id, which is a map of all personas and their locations */
adalyzerControllers.controller('MappingController', ['$scope', function($scope) {
	$scope.title = 'Ads mapping';

	// array with images of personas
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

	// function that runs when the map has initialized
	$scope.$on('mapInitialized', function(event, map) {
		$scope.map = map;
		console.log("Map loaded. Ready to handle new markers");
		add_markers(1, 57.68, 12);
	});

	// initialize an array with markers
	var markers = [];

	// function to add a new marker using img_id which is a persona id,
	// lat and lng of the car / persona
	function add_markers(img_id, lat, lng){
		var marker = new google.maps.Marker({
			title: "car",
			icon: images[img_id]
		});

		var latlng = new google.maps.LatLng(lat, lng);
		marker.setPosition(latlng);
		marker.setMap($scope.map);

		markers.push(marker);			
	}
}]);

adalyzerControllers.controller('StatsController', ['$scope', function($scope) {
	$scope.title = 'Statistics';
}]);