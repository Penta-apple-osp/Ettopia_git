/*  홈 화면에 적용되는 JS 요소
*/

/*버튼 누르면 누른 상태를 유지하고, 다른 버튼 누르면 기존 버튼을 삭제하기*/
function change_btn(e) {
	var btns = document.querySelectorAll(".btn_filter_food");
	btns.forEach(function(btn, i) {
		if(e.currentTarget == btn) {
            if(btn.classList.contains("active")){
                btn.classList.remove("active");
            }
            else{
                btn.classList.add("active");
            }	
		}
		else {
			btn.classList.remove("active");
		}
	});
	//console.log( e.currentTarget );
}

function change_btn_location(e) {
	var btns = document.querySelectorAll(".btn_filter_location");
	btns.forEach(function(btn, i) {
		if(e.currentTarget == btn) {
            if(btn.classList.contains("active")){
                btn.classList.remove("active");
            }
            else{
                btn.classList.add("active");
            }
		}
		else {
			btn.classList.remove("active");
		}
	});
	//console.log( e.currentTarget );
}

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(37.561838, 126.946828), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption); 

// 검색하는 순간 가게 목록 결과가 보이도록 하는 함수
const mapWrap = document.querySelector('#menu_wrap'); //가게 목록 창에 연결
const formSearch = document.querySelector('#form_search'); //가게 목록 창에 연결
const keyword = document.querySelector('#keyword'); //가게 목록 창에 연결
const btnSearch = document.querySelector('#btn_search'); //가게 목록 창에 연결
function showInfoList (){
    //console.log("가게 목록 보여주는 함수 실햄됨");
    mapWrap.classList.add('active');
    formSearch.classList.add('active');
    keyword.classList.add('active');
    btnSearch.classList.add('active');
}

// 각 카테고리 리스트를 클릭하면, 카테고리 이름를 받아서 form으로 제출해주는 함수->라우팅을 위해 사용됨
function categoryChange (dataValue){
    var categoryValue = dataValue;
    document.getElementById('value_category').setAttribute('value', categoryValue);
    document.getElementById('btn_category_info').click();
}

const btnLeft = document.querySelector(".btn_category_left")
btnLeft.onclick = function () {
    var element = document.getElementById('items_filter');
    scrollAmount = 0;
    var slideTimer = setInterval(function(){
        element.scrollLeft -= 10;
        scrollAmount += 10;
        if(scrollAmount >= 100){
            window.clearInterval(slideTimer);
        }
    }, 25);
};

const btnRight = document.querySelector(".btn_category_right")
btnRight.onclick = function () {
    var element = document.getElementById('items_filter');
    scrollAmount = 0;
    var slideTimer = setInterval(function(){
        element.scrollLeft += 10;
        scrollAmount += 10;
        if(scrollAmount >= 100){
            window.clearInterval(slideTimer);
        }
    }, 25);
};

