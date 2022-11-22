/*  홈 화면에 적용되는 JS 요소
    적용 방법
    <script src="홈화면.js" defer></script>
*/

/*버튼 누르면 누른 상태를 유지하고, 다른 버튼 누르면 기존 버튼을 삭제하기*/
function change_btn(e) {
	var btns = document.querySelectorAll(".btn_filter_food");
	btns.forEach(function(btn, i) {
		if(e.currentTarget == btn) {
			btn.classList.add("active");
		}
		else {
			btn.classList.remove("active");
		}
	});
	console.log( e.currentTarget );
}

function change_btn_location(e) {
	var btns = document.querySelectorAll(".btn_filter_location");
	btns.forEach(function(btn, i) {
		if(e.currentTarget == btn) {
			btn.classList.add("active");
		}
		else {
			btn.classList.remove("active");
		}
	});
	console.log( e.currentTarget );
}

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(37.561838, 126.946828), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption); 

