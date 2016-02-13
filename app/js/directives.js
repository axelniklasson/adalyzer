var adalyzerDirectives = angular.module('AdalyzerDirectives', []);

adalyzerDirectives.directive('vehicleMap', function() {
	var link = function(scope, element, attrs) {
		var map, infoWindow;
		var markers = [];

		// config
		var mapOptions = {
			center: new google.maps.LatLng(57.68, 12),
			zoom: 11,
			// mapTypeId: google.maps.MapTypeId.ROADMAP,
			scrollwheel: true
		};

		function initMap() {
			if (map === void 0) {
				map = new google.maps.Map(element[0], mapOptions);
			}
		}

		// place marker
		function setMarker(map, position, title, content) {
			var marker;
			var markerOptions = {
			    position: position,
			    map: map,
			    title: title,
			    icon: 'img/persona-map-1.png'
			};

			marker = new google.maps.Marker(markerOptions);
			markers.push(marker); // add marker to array

			google.maps.event.addListener(marker, 'click', function () {
			    // close window if not undefined
			    if (infoWindow !== void 0) {
			        infoWindow.close();
			    }
			    // create new window
			    var infoWindowOptions = {
			        content: content
			    };
			    infoWindow = new google.maps.InfoWindow(infoWindowOptions);
			    infoWindow.open(map, marker);
			});
		}

		initMap();
	};

	return {
        restrict: 'A',
        template: '<div id="vehicle-map"></div>',
        replace: true,
        link: link
    };
});