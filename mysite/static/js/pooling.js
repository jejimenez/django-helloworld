//angular
//  .module('thinkster', []);

(function () {
  'use strict';

//start page properties
  $('.ui.dropdown').dropdown();

var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
var map;

function initialize() {
  directionsDisplay = new google.maps.DirectionsRenderer();
  var bogota = new google.maps.LatLng(4.754516,-74.046255);
  var mapOptions = {
    zoom: 6,
    center: bogota
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}


google.maps.event.addDomListener(window, 'load', initialize);


//
  angular
    .module('pooling', [
      'pooling.maps',
      ]);


    angular
  .module('pooling')
  .run(run);

  run.$inject = ['$http'];


  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }

})();