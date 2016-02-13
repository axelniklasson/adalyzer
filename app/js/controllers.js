var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices']);

adalyzerControllers.controller('MainController', ['$scope', function($scope) {
	// N/A
}]);

adalyzerControllers.controller('MapController', ['$scope', function($scope) {
	$scope.title = 'Maps';
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