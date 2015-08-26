/**
* GoMaps
* @namespace pooling.maps.services
*/
(function () {
  'use strict';

  angular
    .module('pooling.maps.services')
    .factory('GoMaps', GoMaps);

  GoMaps.$inject = ['$cookies', '$http'];

  /**
  * @namespace GoMaps
  * @returns {Factory}
  */
  function GoMaps($cookies, $http) {
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
      console.log(markers[0].getPosition().lat());
      //toastr["info"]("esta es la funcion de insertar los markers");
        return $http.post('/api/v1/seeker/', {
          user_id : 1,
          start_lat : markers[0].getPosition().lat(),
          start_lng : markers[0].getPosition().lng(),
          end_lat : markers[1].getPosition().lat(),
          end_lnt : markers[1].getPosition().lng(),
      }).then( toastr["info"]("yeeeeeeeeees")); 
    }
 
  }
})();