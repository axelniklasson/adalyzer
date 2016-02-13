var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices']);

adalyzerControllers.controller('MainController', ['$scope', function($scope) {
	// N/A
}]);

adalyzerControllers.controller('MapController', ['$scope', function($scope) {
	$scope.title = 'Maps';
}]);

adalyzerControllers.controller('PersonasController', ['$scope', function($scope) {
	$scope.title = 'Personas';
	$scope.data = [
		{
			'name': 'John Doe',
			'age': '20 y/o'
		},
		{
			'name': 'Jane Doe',
			'age': '20 y/o'
		},
	];
}]);

adalyzerControllers.controller('StatsController', ['$scope', function($scope) {
	$scope.title = 'Stats';
}]);