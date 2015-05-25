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

  //Each time the view is switched to this, retrieve supermanMap
  $scope.map = GoMaps.getMap('supermanMap');

  $scope.editMap = function() {
    $scope.map.kryptonite = true;
  };

    //vm.register = register;
    //activate();
  }
})();