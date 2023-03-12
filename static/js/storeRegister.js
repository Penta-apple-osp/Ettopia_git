/*음식 카테고리의 버튼 누르면 누른 상태를 유지하고, 다른 버튼 누르면 기존 버튼을 삭제하고, 버튼이 눌리는 순간 폼에 제출할 값을 바꾸어준다.*/
function change_btn(e) {
	var btns = document.querySelectorAll(".btn_filter_food");
	btns.forEach(function(btn, i) {
		if(e.currentTarget == btn) {
			btn.classList.add("active");
            document.getElementById('btn_food_hidden').setAttribute('value', btn.value);
            console.log(document.getElementById('btn_food_hidden').value);
		}
		else {
			btn.classList.remove("active");
		}
	});
	console.log( e.currentTarget );
}
/*주차 여부의 버튼 누르면 누른 상태를 유지하고, 다른 버튼 누르면 기존 버튼을 삭제하고, 버튼이 눌리는 순간 폼에 제출할 값을 바꾸어준다.*/
function change_btn_parking(e) {
	var btns = document.querySelectorAll(".btn_filter_park");
	btns.forEach(function(btn, i) {
		if(e.currentTarget == btn) {
			btn.classList.add("active");
            document.getElementById('btn_park_hidden').setAttribute('value', btn.value);
            console.log(document.getElementById('btn_park_hidden').value);
		}
		else {
			btn.classList.remove("active");
		}
	});
	console.log( e.currentTarget );
}

/*드롭다운이 눌리면 해당 숫자가 보이도록 하고, 드롭다운이 눌리는 순간 폼에 제출할 값을 바꾸어준다.*/
/* 매개변수 설명: txtForChange는 드롭다운에서 선택한 값, txtTarget는 선택한 값이 보이는 위치, valueHidden는 폼 제출 시 제출될 hidden 타입 input*/
function view_dropdown_price(txtForChange, txtTarget, valueHidden){
    var txt = txtForChange;
    console.log('드롭다운 클릭: ' + txt);
    var target = txtTarget;
    target.innerHTML = txt;
    
    valueHidden.setAttribute('value', txt); /*폼에 제출할 값 변경*/
}

function view_dropdown_hour(txtForChange, txtTarget, valueHidden){
    var txt = txtForChange;
    console.log('드롭다운 클릭: ' + txt);
    var target = txtTarget;
    target.innerHTML = txt;
    
    valueHidden.setAttribute('value', txt); /*폼에 제출할 값 변경*/
}