var storePosition = document.getElementById('position').value;
storePosition = storePosition.replace('(', '').replace(')', '');
position_splitted = storePosition.split(', ');

//console.log(position_splitted);

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(position_splitted[0], position_splitted[1]), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption); 

// 마커가 표시될 위치입니다 
var markerPosition  = new kakao.maps.LatLng(position_splitted[0], position_splitted[1]); 

// 마커를 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);

