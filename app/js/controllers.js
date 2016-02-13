var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices']);

adalyzerControllers.controller('MainController', ['$scope', function($scope) {
	// N/A
}]);

adalyzerControllers.controller('MapController', ['$scope', function($scope, NgMap) {
	$scope.title = 'Key points';

	$scope.$on('mapInitialized', function(event, map) {
			$scope.map = map;

			var marker = new google.maps.Marker({
    			title: "Hi marker "
  			});
  			var latlng = new google.maps.LatLng(57.68, 12);
  			marker.setPosition(latlng);
  			marker.setMap($scope.map);
		});
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

adalyzerControllers.controller('MappingController', ['$scope', function($scope) {
	$scope.title = 'Mapping';
}]);

adalyzerControllers.controller('StatsController', ['$scope', function($scope) {
	$scope.title = 'Stats';
}]);