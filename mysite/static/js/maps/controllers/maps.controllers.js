/**
* GMaps controller
* @namespace pooling.maps.controllers
*/
(function () {
  'use strict';

  angular
    .module('pooling.maps.controllers')
    .controller('GoMapsController', GoMapsController);

  GoMapsController.$inject = ['$scope'];


  /**
  * @namespace GoMapsController
  */
  function GoMapsController($scope) {
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
  }
})();