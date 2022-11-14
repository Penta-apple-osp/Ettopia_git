const menuBody = document.querySelector('body');
const popupMenu = document.querySelector('.warp_popup_menu');
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

/*등록취소 버튼을 누르면 팝업창 사라짐*/
btnMenuCancel.addEventListener('click', (event) => {
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
}
});