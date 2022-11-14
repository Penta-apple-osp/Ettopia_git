const reviewBody = document.querySelector('body');
const popupReiew = document.querySelector('.warp_popup_review');
const btnReviewCancel = document.querySelector('.btn_review_cancel');
const btnReviewRegister = document.querySelector('.btn_review_register');
const btnAddReview = document.querySelector('.btn_add_review');

/*버튼을 누르면 팝업창을 보여준다*/
btnAddReview.addEventListener('click', () => {
    popupReiew.classList.toggle('show');

if (popupReiew.classList.contains('show')) {
    /*reviewBody.style.overflow = 'hidden';*/
}

});

/*등록취소 버튼을 누르면 팝업창 사라짐*/
btnReviewCancel.addEventListener('click', (event) => {
if (event.target === btnReviewCancel) {
    popupReiew.classList.toggle('show');

    if (!popupReiew.classList.contains('show')) {
        reviewBody.style.overflow = 'auto';
        reviewBody.style.overflowX = 'hidden';
    }
}
});

/*등록하기 버튼을 누르면 팝업창 사라짐*/
btnReviewRegister.addEventListener('click', (event) => {
if (event.target === btnReviewRegister) {
    popupReiew.classList.toggle('show');

    if (!popupReiew.classList.contains('show')) {
        reviewBody.style.overflow = 'auto';
        reviewBody.style.overflowX = 'hidden';
    }
}
});