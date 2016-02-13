var adalyzerControllers = angular.module('AdalyzerControllers', ['AdalyzerServices']);

adalyzerControllers.controller('MainController', ['$scope', function($scope) {
	$scope.title = 'Hello World!';
}]);