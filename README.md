# Ettopia_git
이화여대 맛집 커뮤니티 웹사이트 'Ettopia'의 최종 프론트엔드 개발(html, css) 및 벡엔드 개발(flask, liteDB)를 담당하는 레포지토리입니다. 해당 README.md는 펜타애플 팀의 Ettopia를 개발하며 작성한 프론트엔드 및 백엔드 관련 코드를 push한 Ettopia_git의 마크다운 파일입니다.


## *Ettopia의 개발 툴 및 오픈소스 소프트웨어*
Ettopia의 프론트엔드 개발에서는 팀원 별 개발 파트를 나누어 VS code를 사용하여 코드 작성 후 Github를 통해 코드를 취합했고, 백엔드 개발에서는 GoormIDE에서 Flask를 사용해 Ettopia 개발을 진행하였습니다.
사용한 개발 툴 및 오픈소스 소프트웨어에 대한 자세한 설명 및 사용방법은 하단의 링크를 통해 확인할 수 있습니다.

[펜타애플 티스토리: Flask 설명](https://pentaapple.tistory.com/2)

[펜타애플 티스토리: 구름IDE 사용방법](https://pentaapple.tistory.com/5)


## *Ettopia의 데이터베이스*
Ettopia에서 사용자가 입력한 정보를 저장하고 추후 여러 기능을 위해 저장된 정보들을 불러오는 데이터베이스로 firebase database를 사용했습니다. **직관적으로 어떠한 방식으로 정보가 저장되어 있는 지 확인할 수 있는 장점**을 가졌으나, **키값-속성을 한 쌍씩 무조건 가져야 하며 상대적으로 제한적인 기능을 가진다는 단점**을 지니고 있기 때문에 추후 사용에 유의하시기 바랍니다.
데이터베이스와의 연결 및 정보전달 등의 코드 부분은 js 파일과 py 파일의 코드를 통해 확인할 수 있습니다.

## *Ettopia의 특별한 기능 - 지도 API*
Ettopia에는 다양한 기능이 존재하지만 그 중 개발 기간에 상당 부분을 차지했던 맛집 지도 기능을 개발할 때 카카오 지도 API를 사용하였습니다. 해당 API는 homePage.html, storeDetail.html에서 활용되었으며 맛집의 위치와 종류에 따라 필터링하여 지도 상에서 사용자가 찾고자하는 맛집을 쉽게 볼 수 있도록 구현하였습니다. 필터링에 대한 자세한 코드는 homePage.html에서 확인할 수 있습니다.

[펜타애플 티스토리: 카카오 지도 API 응용](https://pentaapple.tistory.com/10)
