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
      addMap: addMap,
      getMap: getMap,
    };

    return GoMaps;



    ////////////////////
  function addMap(mapId) {
    
    var mapOptions = {
        zoom: 4,
        center: new google.maps.LatLng(40.0000, -98.0000),
        mapTypeId: google.maps.MapTypeId.TERRAIN
    }
    //Data
    /*
var cities = [
    {
        city : 'Toronto',
        desc : 'This is the best city in the world!',
        lat : 43.7000,
        long : -79.4000
    },
    {
        city : 'New York',
        desc : 'This city is aiiiiite!',
        lat : 40.6700,
        long : -73.9400
    },
    {
        city : 'Chicago',
        desc : 'This is the second best city in the world!',
        lat : 41.8819,
        long : -87.6278
    },
    {
        city : 'Los Angeles',
        desc : 'This city is live!',
        lat : 34.0500,
        long : -118.2500
    },
    {
        city : 'Las Vegas',
        desc : 'Sin City...\'nuff said!',
        lat : 36.0800,
        long : -115.1522
    }
];*/


    tmap = new google.maps.Map(document.getElementById(mapId), mapOptions);

    markers = [];
    
    var infoWindow = new google.maps.InfoWindow();
    /*
    var createMarker = function (info){
        
        var marker = new google.maps.Marker({
            map: tmap,
            position: new google.maps.LatLng(info.lat, info.long),
            title: info.city
        });
        marker.content = '<div class="infoWindowContent">' + info.desc + '</div>';
        
        google.maps.event.addListener(marker, 'click', function(){
            infoWindow.setContent('<h2>' + marker.title + '</h2>' + marker.content);
            infoWindow.open(tmap, marker);
        });
        
        markers.push(marker);
        
    }  
    
    for (var i = 0; i < cities.length; i++){
        createMarker(cities[i]);
    }*/

    /*$scope.openInfoWindow = function(e, selectedMarker){
        e.preventDefault();
        google.maps.event.trigger(selectedMarker, 'click');
    }*/
    //tmap = map;

  //google.maps.event.addDomListener(window, 'load', initialize);
  maps[mapId] = tmap;
    return tmap;
  }


  function getMap(mapId) {
    if (!maps[mapId]) addMap(mapId);
    return maps[mapId];
  }
  /*
  function getMap(mapId) {
    //if (!mapId]) 
      addMap(mapId);
    return tmap;
  }*/
 
  }
})();