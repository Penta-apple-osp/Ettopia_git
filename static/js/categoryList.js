function pageChange (page){
    //console.log("함수 실행됨")
    var pageNum = page
    document.getElementById('page').setAttribute('value', pageNum);
    document.getElementById('btn_category_info').click();
}