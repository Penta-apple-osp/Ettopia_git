/*해당 JS는 이미지를 업로드하고 삭제하는 기능을 통합적으로 관리합니다.
  storeRegister, menuRegister, reviewRegister 화면에서 호출합니다.
 */

/*이미지 파일 업로드하면 화면에 보여주기*/
function loadFile(input, imgTemp, imgContainer, btnUpload, btnDelete) {
    console.log('imgUploadDelete.js의 loadFile 함수 호출');
    
    var file = input.files[0];	//선택된 파일 가져오기

    //미리 만들어 놓은 이미지 div 에 이미지 보이기
    //var newImage = document.getElementById("img_store_temp");
    var newImage = imgTemp;

    //이미지 source 가져오기
    newImage.src = URL.createObjectURL(file);
    
    newImage.style.visibility = "visible"; //화면에 보이게 만든다.
    newImage.style.width = "100%";
    newImage.style.objectFit = "cover";
    newImage.style.position = "absolute";
    //이미지 중심축 기준으로 보이게 만든다.
    newImage.style.top = "50%"; 
    newImage.style.left = "50%";
    newImage.style.transform = "translate(-50%, -50%)";

   //기존의 border 없애고 새로운 이미지를 첫 번째 자식 요소로 넣기
    var container = imgContainer;
    container.style.border = "none";

    //업로드 버튼 더 이상 안 보이게 하기
    var childNodes = btnUpload.getElementsByTagName('*');
    for (var node of childNodes) {
        node.style.visibility = "hidden";
    }

    //삭제 버튼 보이게 하기
    var childNodes = btnDelete.getElementsByTagName('*');
    for (var node of childNodes) {
        node.style.visibility = "visible";
    }
};


function deleteFile(imgOld, btnUpload, fileChoose, imgContainer, btnDelete) {
    console.log('imgUploadDelete.js의 deleteFile 함수 호출');
    //기존 이미지 삭제
    var oldImage = imgOld;
    URL.revokeObjectURL(oldImage.src);
    oldImage.src = "";

    //업로드 버튼 다시 보이게 하기
    var childNodes = btnUpload.getElementsByTagName('*');
    for (var node of childNodes) {
        node.style.visibility = "visible";
    }

    var chooseFile = fileChoose;
    chooseFile.style.visibility = "hidden";

    //border 다시 보이게 하기
    var container = imgContainer;
    container.style.border = "2px dashed var(--common-light-grey)";

    //삭제 버튼 더 이상 안 보이게 하기
    var childNodes = btnDelete.getElementsByTagName('*');
    for (var node of childNodes) {
        node.style.visibility = "hidden";
    }
};