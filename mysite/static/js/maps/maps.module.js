(function () {
  'use strict';

  angular
    .module('pooling.maps', [
      'pooling.maps.controllers',
      'pooling.maps.services'
    ]);

  angular
    .module('pooling.maps.controllers', []);

  angular
    .module('pooling.maps.services', ['ngCookies']);
})();