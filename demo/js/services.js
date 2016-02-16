var adalyzerServices = angular.module('AdalyzerServices', []);

adalyzerServices.factory('BackendService', ['$http', function($http) {
	var URL = 'http://localhost:5000';

	return {
		history: function() {
			return $http.get(URL + '/history');
		},
		personas: function() {
			return $http.get(URL + '/personas');
		}
	};
}]);