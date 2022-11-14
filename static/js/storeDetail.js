var mapContainer = document.getElementById('map'),
    mapOption = {
        center: new kakao.maps.LatLng(37.561838, 126.946828), 
        level: 4
    };


var map = new kakao.maps.Map(mapContainer, mapOption); 