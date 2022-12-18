const menuBody = document.querySelector('body');
const popupMenu = document.querySelector('.wrap_popup_menu');
const btnMenuCancel = document.querySelector('.btn_menu_cancel');
const btnMenuRegister = document.querySelector('.btn_menu_register');
const btnAddMenu = document.querySelector('.btn_add_menu');

/*버튼을 누르면 팝업창을 보여준다*/
btnAddMenu.addEventListener('click', () => {
    popupMenu.classList.toggle('show');

if (popupMenu.classList.contains('show')) {
    /*menuBody.style.overflow = 'hidden';*/
}

});

/*등록취소 버튼을 누르면 등록한 정보 사라지고, 팝업창 사라짐*/
btnMenuCancel.addEventListener('click', (event) => {

    var inputName = document.getElementsByClassName('txt_input_name');
    var inputPrice = document.getElementsByClassName('txt_input_price');
    for(var i=0; i<inputName.length; i++){
	    inputName[i].value = '';
    }
    for(var i=0; i<inputPrice.length; i++){
	    inputPrice[i].value = '';
    }

    if (event.target === btnMenuCancel) {
        popupMenu.classList.toggle('show');

        if (!popupMenu.classList.contains('show')) {
            menuBody.style.overflow = 'auto';
            menuBody.style.overflowX = 'hidden';
        }
    }
});

/*등록하기 버튼을 누르면 팝업창 사라짐*/
btnMenuRegister.addEventListener('click', (event) => {
if (event.target === btnMenuRegister) {
    popupMenu.classList.toggle('show');

    if (!popupMenu.classList.contains('show')) {
        menuBody.style.overflow = 'auto';
        menuBody.style.overflowX = 'hidden';
    }
    
    var inputName = document.getElementsByClassName('txt_input_name')[0].value;
    var inputPrice = document.getElementsByClassName('txt_input_price')[0].value;
    var infoMenu = document.querySelector('.txt_init_menu');
    var infoPrice = document.querySelector('.txt_menu_price_show');
    //console.log(inputName)
    if(typeof(infoMenu) != 'undefined' && infoMenu != null){
        infoMenu.innerText = inputName;
        infoPrice.innerText = inputPrice;
    }
}
});