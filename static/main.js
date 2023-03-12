/*모든 파일의 title 설정*/
document.title = "Ettopia, 맛집 커뮤니티";

/*모든 파일의 header 관련 함수*/
const menuBtn = document.querySelector('.btn_nav_menu'); //버튼에 연결
const menu = document.querySelector('.list_nav'); //메뉴에 연결

/*
menuBtn.addEventListener('click', ()=> {  //클릭하는 순간 다음 함수 실행: active가 없다면 추가해주고, 있으면 삭제해줌
    menu.classList.toggle('active');
});
*/

const wrapProfile = document.querySelector('.wrap_myprofile'); //버튼에 연결
const boxProfile = document.querySelector('.profilebox'); //프로필 영역에 클릭
const icon = document.getElementById("icon");
wrapProfile.addEventListener('click', ()=> {  //클릭하는 순간 다음 함수 실행: active가 없다면 추가해주고, 있으면 삭제해줌
    wrapProfile.classList.toggle('open');
    boxProfile.classList.toggle('open');
    icon.innerText = wrapProfile.classList.contains('open') ? "close" : "expand_more";
});

const profile = document.querySelector('.profilebox');
window.addEventListener('scroll', function() {
	if (window.pageYOffset > 8) {
		profile.style.top = "52px";
	} else{
        profile.style.top = "60px";
    }
});