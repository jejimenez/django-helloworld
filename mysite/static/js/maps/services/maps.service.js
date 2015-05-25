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
    var GoMaps = {
      addMap: addMap,
      getMap: getMap,
    };

    return GoMaps;

    ////////////////////
  function addMap(mapId) {
    maps[mapId] = {};
  }
  function getMap(mapId) {
    if (!maps[mapId]) addMap(mapId);
    return maps[mapId];
  }

 
  }
})();