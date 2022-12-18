const section = document.querySelector("section");
const profileBody = document.querySelector('body');
const popupProfile = document.querySelector('.wrap_popup_profile');
const btnProfileCancel = document.querySelector('.btn_profile_cancel');
const btnChangeProfile = document.querySelector('.btn_modify_profile');
const btnReviewRegister = document.querySelector('.btn_profile_register');
const inputProfile = document.querySelector('#profile_change');

/*flip page 부분
let clicked = false;  
section.addEventListener("click", (e) => {  
 section.classList.toggle("flip");  
 if (!clicked) {  
  clicked = true;  
  document.getElementById("title").style.opacity = 0;  
 }  
}); 
*/

/*팝업창 생성 부분*/
btnChangeProfile.addEventListener('click', () => {
    popupProfile.classList.toggle('show');

    if (popupProfile.classList.contains('show')) {
    }

});

/*등록취소 버튼을 누르면 등록한 정보 사라지고, 팝업창 사라짐*/
btnProfileCancel.addEventListener('click', (event) => {
    //console.log("addEventListener 실행됨")

    if (event.target === btnProfileCancel) {
        //console.log("if 문 실행됨")
        popupProfile.classList.toggle('show');

        if (!popupProfile.classList.contains('show')) {
            //console.log("profileBody overflow 실행됨")
            profileBody.style.overflow = 'auto';
            profileBody.style.overflowX = 'hidden';
        }
    }
});

/*등록하기 버튼을 누르면 팝업창 사라짐*/
btnProfileRegister.addEventListener('click', (event) => {
if (event.target === btnProfileRegister) {
    popupProfile.classList.toggle('show');

    if (!popupProfile.classList.contains('show')) {
        ProfileBody.style.overflow = 'auto';
        ProfileBody.style.overflowX = 'hidden';
    }
}
});

function borderImg(e) {
	var profiles = document.querySelectorAll(".profile");
	profiles.forEach(function(profile, i) {
		if(e.currentTarget == profile) { //클릭 이벤트가 일어난 버튼이라면
            if(profile.classList.contains('clicked')){ //클릭 이벤트가 일어났는데 이미 기존에도 눌려 있는 상태라면
                profile.classList.remove('clicked'); //버튼 눌린 상태 취소
            }
            else{   //클릭 이벤트가 일어났는데 기존에 안 눌려 있는 상황이었다면
                profile.classList.add('clicked'); //버튼을 눌러 줌
                inputProfile.value = profile.id;
            } //else 문의 괄호입니다
		} //if문의 괄호입니다
		else { //클릭 이벤트가 안 일어난 버튼이라면
			profile.classList.remove('clicked'); //기존에 버튼이 눌려 있었더라도 취소해줌
		}
	}); //for 문의 괄호입니다
}