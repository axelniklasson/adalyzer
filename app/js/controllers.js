var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices', 'AdalyzerDirectives']);

adalyzerControllers.controller('MainController', ['$scope', function($scope) {
	// N/A
}]);

adalyzerControllers.controller('MapController', ['$scope', function($scope, NgMap) {
	$scope.title = 'Key points';

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

	$scope.$on('mapInitialized', function(event, map) {
		$scope.map = map;
		console.log("Map loaded. Ready to handle new markers");
		add_markers(1, 57.68, 12);
	});

	var markers = [];

	function add_markers(img_id, lat, lng){
		var marker = new google.maps.Marker({
			title: "car",
			icon: images[img_id]
		});

		var latlng = new google.maps.LatLng(lat, lng);
		marker.setPosition(latlng);
		marker.setMap($scope.map);

		markers.push(marker);			
	};
	

}]);

adalyzerControllers.controller('PersonasController', ['$scope', function($scope) {
	$scope.title = 'Personas';
	var data = [
		{
			'name': 'John Doe',
			'age': '20 y/o',
			'interests': [
				'Foo', 'Bar', 'Baz'
			]
		},
		{
			'name': 'Jane Doe',
			'age': '20 y/o',
			'interests': [
				'Foo', 'Bar', 'Baz'
			]
		},
		{
			'name': 'Steve Jobs',
			'age': '20 y/o',
			'interests': [
				'Foo', 'Bar', 'Baz'
			]
		},
		{
			'name': 'Steve Wozniak',
			'age': '20 y/o',
			'interests': [
				'Foo', 'Bar', 'Baz'
			]
		},
	];

	angular.forEach(data, function(value, key) {
		value.img = 'img/persona-' + (key + 1) + '.png';
	});
	
	$scope.personas = data;
}]);

adalyzerControllers.controller('StatsController', ['$scope', function($scope) {
	$scope.title = 'Stats';
}]);