/**
* GoMaps
* @namespace pooling.maps.services
*/
(function () {
  'use strict';

  angular
    .module('pooling.maps.services')
    .factory('GoMaps', GoMaps);

  GoMaps.$inject = ['$cookies'];

  /**
  * @namespace GoMaps
  * @returns {Factory}
  */
  function GoMaps($cookies) {
    /**
    * @name GoMaps
    * @desc The Factory to be returned
    */
    var maps = {};
    var tmap;
    var markers;
    var GoMaps = {
      setMarkersSeeker: setMarkersSeeker,
    };

    return GoMaps;


    function setMarkersSeeker(markers) {
      console.log(markers);
      toastr["info"]("setMarkersSeeker");
    }
 
  }
})();