# Ettopia_git
이화여대 맛집 커뮤니티 웹사이트 'Ettopia'의 최종 프론트엔드 개발(html, css) 및 벡엔드 개발(flask, liteDB)를 담당하는 레포지토리입니다. 해당 README.md는 펜타애플 팀의 Ettopia를 개발하며 작성한 프론트엔드 및 백엔드 관련 코드를 push한 Ettopia_git의 마크다운 파일입니다.

🥘 프로젝트 ‘Ettopia’는 사용자의 편의성 증대와 강한 커뮤니티 소속감 제공을 지향합니다.

[![](스크린샷 이미지)](https://drive.google.com/file/d/1OGPVGY9gl9SiaOL2-yxsUWAlw7hD--Ml/view?usp=share_link" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture)

## *Ettopia의 개발 툴 및 오픈소스 소프트웨어*
Ettopia의 프론트엔드 개발에서는 팀원 별 개발 파트를 나누어 VS code를 사용하여 코드 작성 후 Github를 통해 코드를 취합했고, 백엔드 개발에서는 GoormIDE에서 Flask를 사용해 Ettopia 개발을 진행하였습니다.
사용한 개발 툴 및 오픈소스 소프트웨어에 대한 자세한 설명 및 사용방법은 하단의 링크를 통해 확인할 수 있습니다.

[펜타애플 티스토리: Flask 설명](https://pentaapple.tistory.com/2)

[펜타애플 티스토리: 구름IDE 사용방법](https://pentaapple.tistory.com/5)

## *프로젝트 구조*

‘Ettopia’는 flask를 활용하여 구현한 프로젝트입니다. 따라서 flask framework에서 사용하는 프로젝트 구조를 활용합니다. 구체적으로는 다음과 같습니다.

```python
Ettopia
├── 📁authentication
│   └── firebase_auth.json
├── 📁static
│   ├── 📁css
│   ├── 📁js
│   ├── 📁icon
│   ├── 📁img
│   ├── 📁img_user
│   ├── 📁logo
│   ├── 📁profile
│   ├── main.js
│   └── style.css
├── 📁templates
│   ├── 파일명.html
│   └── ...
├── application.py
└── database.py
```

해당 구조의 설명은 다음과 같습니다.

- 📁authentication: firebase를 사용하기 위해서 필요한 인증 json 파일을 담고 있는 폴더입니다. 해당 폴더 안의 파일은 firebase 계정 별로 고유한 키를 통해 사용해야 합니다.
- 📁static: 프로젝트를 사용함에 있어서 변동이 없는 파일들을 담는 폴더입니다. 대표적으로는 css, js 파일과 png, jpeg 등의 이미지 파일이 있습니다.
    - 📁 css: 프로젝트에 사용되는 html 파일에 필요한 스타일 요소를 관리하는 폴더입니다.
    - 📁 js: 프로젝트에 사용되는 html 파일에 필요한 자바 스크립트 요소를 관리하는 폴더입니다.
    - 📁 img_user: 사용자가 ‘Ettopia’를 사용하면서 업로드하는 이미지를 저장해 놓는 폴더입니다. 따로 database를 구축하여 이미지 요소를 관리할 경우, 해당 폴더는 필요하지 않습니다.
    - 📁 기타 폴더: 프로젝트에 필요한 이미지 요소를 저장해 놓은 폴더입니다.
    - main.js/style.css: 모든 html 파일에 기본적으로 적용되어야 하는 스타일/자바 스크립트 요소를 관리하는 파일입니다. 다른 폴더와 같은 level, 즉 static 폴더 바로 아래에 있어야 합니다.
- 📁templates: 프로젝트에서 사용된 모든 html 파일들을 관리하는 폴더입니다. flask의 구조 상, 모든 html 파일들은 반드시 해당 폴더 아래에 있어야 합니다.

## *Ettopia의 데이터베이스*
Ettopia에서 사용자가 입력한 정보를 저장하고 추후 여러 기능을 위해 저장된 정보들을 불러오는 데이터베이스로 firebase database를 사용했습니다. **직관적으로 어떠한 방식으로 정보가 저장되어 있는 지 확인할 수 있는 장점**을 가졌으나, **키값-속성을 한 쌍씩 무조건 가져야 하며 상대적으로 제한적인 기능을 가진다는 단점**을 지니고 있기 때문에 추후 사용에 유의하시기 바랍니다.
‘Ettopia’를 위해 구현한 firebase DB의 구조와 각각의 설명은 다음 그림과 같습니다. 해당 구조는 각자의 프로젝트의 적합하게 변경하거나, 다르게 구현하셔도 됩니다. 그러나 위에서 소개한 database.py는 현재 프로젝트의 firebase 구조에서 데이터를 조회하고 저장하는 코드가 구현되어 있어 변경하셔야 합니다.
![firebase](https://github.com/Penta-apple-osp/Ettopia_git/blob/Final/firebase.png)


## *Ettopia의 특별한 기능 - 지도 API*
Ettopia에는 다양한 기능이 존재하지만 그 중 개발 기간에 상당 부분을 차지했던 맛집 지도 기능을 개발할 때 카카오 지도 API를 사용하였습니다. 해당 API는 homePage.html, storeDetail.html에서 활용되었으며 맛집의 위치와 종류에 따라 필터링하여 지도 상에서 사용자가 찾고자하는 맛집을 쉽게 볼 수 있도록 구현하였습니다. 필터링에 대한 자세한 코드는 homePage.html에서 확인할 수 있습니다.

[펜타애플 티스토리: 카카오 지도 API 응용](https://pentaapple.tistory.com/10)
