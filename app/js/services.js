var adalyzerServices = angular.module('AdalyzerServices', []);

adalyzerServices.factory('BackendService', function() {
	return {
		subscribe: function(scope, callback) {
			var handler = $rootScope.$on('data-received', callback);
			scope.$on('$destroy', handler);
		},

		notify: function() {
			$rootScope.$emit('data-received');
		}
	};
});