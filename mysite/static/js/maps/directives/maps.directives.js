/**
* GoMaps
* @namespace pooling.maps.directives
*/
(function () {
  'use strict';

angular.module('pooling.maps.directives', [])
.directive('gMap', gMapDirective);


  gMapDirective.$inject = ['$window', '$parse'];


    function gMapDirective($window,$parse) {
        var counter = 0,
        prefix = '__ep_gmap_',
        img_start_rt = 'http://maps.google.com/mapfiles/kml/paddle/go.png',
        img_end_rt = 'http://maps.google.com/mapfiles/kml/paddle/ylw-square.png',
        str_start_rt = 'Inicio de ruta',
        str_end_rt = 'Fin de ruta'/*,
        goldStarSVG = {
            path: 'M 125,5 155,90 245,90 175,145 200,230 125,180 50,230 75,145 5,90 95,90 z',
            fillColor: 'yellow',
            fillOpacity: 0.8,
            scale: 0.1,
            strokeColor: 'gold',
            strokeWeight: 3
          }*/;

        return {
            restrict: 'E',
            replace: false,
            controller: 'GoMapsController',
            scope: {idmap: '@'},
            templateUrl: 'static/templates/maps/gmap.html',
            link: function (scope, element, attrs, controller) {
                var model = scope.gmap;
                console.log(scope);
                if ($window.google && $window.google.maps) {
                    gMapInit();
                } else {
                    injectGoogle();
                };
                function gMapInit() {
                   var 
                    directionsDisplay = new google.maps.DirectionsRenderer({
                        draggable: true
                    }),
                    mapOptions = {
                            center: new google.maps.LatLng(model.Lat, model.Lon),
                            zoom: 11,
                            mapTypeId: google.maps.MapTypeId.ROADMAP
                        },
                    map = new google.maps.Map(document.getElementById(attrs.idmap),mapOptions),
                    markers = [];
                    // add your fixed business marker
                    directionsDisplay.setMap(map);
                    google.maps.event.addListener(map, 'click', function(event) {
                       placeMarker(event.latLng);
                    });

                    // Try HTML5 geolocation
                    if ("geolocation" in navigator) {
                        navigator.geolocation.getCurrentPosition(function (position) {
                            var pos = new google.maps.LatLng(position.coords.latitude,
                                                             position.coords.longitude);
                            map.setCenter(pos);
                            scope.$apply(function () {
                                model.fromAddress = pos;
                            });
                        });
                    }
                    google.maps.event.addListener(directionsDisplay, 'directions_changed', function () {});

                    /**
                    * place the markers. Just two markers, start rout and end rout.
                    **/
                    function placeMarker(location) {
                        var 
                            marker = new google.maps.Marker({
                                position: location, 
                                map: map,
                                animation: google.maps.Animation.DROP,
                                draggable:true                                
                                //icon: 'http://maps.google.com/mapfiles/kml/paddle/go.png',
                            });
                        if(markers.length >= 1 ){
                            marker.setIcon(img_end_rt);
                            marker.setTitle(str_start_rt);   
                            if(markers.length > 1){
                                markers[1].setMap(null);
                                markers.splice(1);
                            }
                        }
                        else{
                            marker.setTitle(str_end_rt);
                            marker.setIcon(img_start_rt);
                        }
                        markers.push(marker);
                    }
                };
                function injectGoogle() {
                    var cbId = prefix + ++counter;
                    $window[cbId] = gMapInit;
                    var wf = document.createElement('script');
                    wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
                    '://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' + 'callback=' + cbId;
                    wf.type = 'text/javascript';
                    wf.async = 'true';
                    var s = document.getElementsByTagName('script')[0];
                    s.parentNode.insertBefore(wf, s);

                    toastr["success"]("Mapa cargado");
                };
            }
        }
    }

})();