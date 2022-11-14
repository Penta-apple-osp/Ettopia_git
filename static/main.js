/*모든 파일의 title 설정*/
document.title = "Ettopia, 맛집 커뮤니티";

/*모든 파일의 header 관련 함수*/
const menuBtn = document.querySelector('.btn_nav_menu'); //버튼에 연결
const menu = document.querySelector('.list_nav'); //메뉴에 연결

menuBtn.addEventListener('click', ()=> {  //클릭하는 순간 다음 함수 실행: active가 없다면 추가해주고, 있으면 삭제해줌
    menu.classList.toggle('active');
});