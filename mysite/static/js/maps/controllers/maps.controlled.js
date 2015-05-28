/**
* GMaps controller
* @namespace pooling.maps.controllers
*/
(function () {
  'use strict';

  angular
    .module('pooling.maps.controllers')
    .controller('GoMapsController', GoMapsController);

  GoMapsController.$inject = ['$location', '$scope', 'GoMaps'];


  /**
  * @namespace GoMapsController
  */
  function GoMapsController($location, $scope, GoMaps) {


    var vm = this;
    var directionsDisplay;
    var directionsService = new google.maps.DirectionsService();
    var map;

function initialize() {/*
  directionsDisplay = new google.maps.DirectionsRenderer();
  var bogota = new google.maps.LatLng(4.754516,-74.046255);
  var mapOptions = {
    zoom: 6,
    center: bogota
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);*/
  $scope.map = GoMaps.getMap('map-canvas');

}


google.maps.event.addDomListener(window, 'load', initialize);

  //Each time the view is switched to this, retrieve supermanMap
  //$scope.map = GoMaps.getMap('map-canvas');



  $scope.editMap = function() {
    $scope.map.kryptonite = true;
  };

    //vm.register = register;
    //activate();
  }
})();