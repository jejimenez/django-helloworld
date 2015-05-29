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

function initMap() {
  $scope.map = GoMaps.getMap('map-canvas');

}


//google.maps.event.addDomListener(window, 'load', initMap);

  //Each time the view is switched to this, retrieve supermanMap
  //$scope.map = GoMaps.getMap('map-canvas');



  $scope.editMap = function() {
    $scope.map.kryptonite = true;
  };

    //vm.register = register;
    //activate();
  }
})();