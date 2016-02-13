var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices']);

adalyzerControllers.controller('MainController', ['$scope', function($scope) {
	// N/A
}]);

adalyzerControllers.controller('MapController', ['$scope', function($scope) {
	$scope.title = 'Maps';
}]);

adalyzerControllers.controller('PersonasController', ['$scope', function($scope) {
	$scope.title = 'Personas';
}]);

adalyzerControllers.controller('StatsController', ['$scope', function($scope) {
	$scope.title = 'Stats';
}]);