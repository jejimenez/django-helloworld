/**
* GMaps controller
* @namespace pooling.maps.controllers
*/
(function () {
  'use strict';

  angular
    .module('pooling.maps.controllers')
    .controller('GoMapsController', GoMapsController);

  GoMapsController.$inject = ['$scope', 'GoMaps'];


  /**
  * @namespace GoMapsController
  */
  function GoMapsController($scope, GoMaps) {

    $scope.gmap = {
      fromAddress: 'Calgary',
      streetAddress: "5111 47 St NE  Calgary, AB T3J 3R2",
      businessWriteup: "<b>Calgary Police Service</b><br/>Calgary's Finest<br/>",
      businessTitle: "Calgary Police Service",
      Lon: -74.0574995,
      Lat: 4.6519047,
      //idmap: $attr.idmap,
      showError: function (status) {
          toastr.error(status);
      }
    };

    /**
    * @name saveMarkersSeeker
    * @desc save the markers of transport seeker
    * @memberOf pooling.maps.controllers
    */
    
    $scope.saveMarkersSeeker = function() {
      if(!$scope.gmap.markers || $scope.gmap.markers.length != 2){toastr['error']('Por favor seleccione los puntos de inicio y fin de la ruta deseada'); return null;}
        GoMaps.setMarkersSeeker($scope.gmap.markers);
    };

    $scope.showMessage = function (){
      toastr['error']('::'+$('#map_canvas').length); return null;
    };
  }
})();